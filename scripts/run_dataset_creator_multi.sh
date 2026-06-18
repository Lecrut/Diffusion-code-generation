#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

OLLAMA_URL_DEFAULT="http://10.24.16.27:11434"
MODELS=(
  "qwen3.6:27b"
  "qwen3.6:35b"
  "qwen3.5:122b-a10b"
)

for model in "${MODELS[@]}"; do
  safe_model="${model//:/_}"
  data_dir="runs/${safe_model}"
  log_file="${data_dir}/run.log"
  mkdir -p "$data_dir"

  echo "Starting model=${model} data_dir=${data_dir}"
  (
    export OLLAMA_URL="${OLLAMA_URL:-$OLLAMA_URL_DEFAULT}"
    export OLLAMA_MODEL="$model"
    export DATASET_CREATOR_DATA_DIR="$data_dir"
    export DATASET_CREATOR_MAX_WORKERS="3"
    python src/dataset-creator/dataset-generator.py > "$log_file" 2>&1
  ) &
done

wait
echo "All runs finished."
