from pathlib import Path

# Central location for generated dataset artifacts.
DATA_PATH = Path(__file__).resolve().parent.parent.parent / "data"

# Backward-compatible alias for older imports.
DATA_DIR = DATA_PATH