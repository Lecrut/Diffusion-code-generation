# Diffusion Code Generation

Repozytorium do budowy wieloagentowego systemu dyfuzyjnego generowania kodu.

## Struktura src

- src/llm/connect.py - wspolne polaczenie do Gemini API
- src/llm/planer.py - Modul 1, planner korzystajacy ze wspolnego polaczenia
- src/planer.py - prosty punkt wejscia do szybkiego uruchomienia


## Artykuły naukowe 

- DIFFUCODER: UNDERSTANDING AND IMPROVING MASKED DIFFUSION MODELS FOR CODE GENERATION
- - https://arxiv.org/pdf/2506.20639
- CodeFusion: A Pre-trained Diffusion Model for Code Generation
- - https://openreview.net/forum?id=I9DVeu8XKa
- Rozwiązanie Googla
- - https://deepmind.google/models/gemini-diffusion/
- Discrete Diffusion do tekstu
- - https://github.com/ash80/diffusion-gpt/blob/master/The_Annotated_Discrete_Diffusion_Models.ipynb


## Datasety

- - https://huggingface.co/datasets/flytech/python-codes-25k

## Wznawianie treningu z checkpointu

Trening zapisuje najlepszy model oraz `last.ckpt` w katalogu `CHECKPOINT_DIR`.
Ustaw `AUTO_RESUME_LAST=1`, aby automatycznie wznowic trening z
`CHECKPOINT_DIR/last.ckpt`, jesli ten plik istnieje:

```powershell
$env:AUTO_RESUME_LAST="1"
python src/train.py
```

Mozesz tez wskazac konkretny checkpoint. `RESUME_CHECKPOINT_PATH` ma pierwszenstwo
przed `AUTO_RESUME_LAST`:

```powershell
$env:RESUME_CHECKPOINT_PATH="checkpoints/last.ckpt"
python src/train.py
```

