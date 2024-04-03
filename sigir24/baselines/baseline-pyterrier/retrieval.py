#!/usr/bin/env python3
# Load a patched ir_datasets that loads the injected data inside the TIRA sandbox
from tira.third_party_integrations import ensure_pyterrier_is_loaded, persist_and_normalize_run
import pyterrier as pt
from tira.rest_api_client import Client

ensure_pyterrier_is_loaded()
tira = Client()

# In the TIRA sandbox, this is the injected ir_dataset, injected via the environment variable TIRA_INPUT_DIRECTORY
pt_dataset = pt.get_dataset('irds:reneuir-2024/tiny-sample-20231030-training')

index = tira.pt.index('ir-benchmarks/tira-ir-starter/Index (tira-ir-starter-pyterrier)', 'tiny-sample-20231030-training')

bm25 = pt.BatchRetrieve(index, wmodel="BM25", verbose=True)

print('Create run')
run = bm25(pt_dataset.get_topics("title"))
print('Done, run was created')

# In the TIRA sandbox, this uses an environment variable to persist the run to the correct output directory
persist_and_normalize_run(run, 'bm25-default_weights')    
