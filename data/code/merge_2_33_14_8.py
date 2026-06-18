import json
import logging
from pathlib import Path
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
class NameVerifier:
    def __init__(self, data_source_path: str):
        self.data_source_path = Path(data_source_path)
    def _load_data(self) -> list[dict]:
        if not self.data_source_path.exists():
            logger.error(f"Data file not found at {self.data_source_path}")
            return []
        try:
            with open(self.data_source_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if isinstance(data, list):
                    return [item.get('name', '') for item in data]
                elif isinstance(data, dict):
                    return [data.get('name', '')]
        except (json.JSONDecodeError, IOError) as e:
            logger.error(f"Failed to load data from {self.data_source_path}: {e}")
        return []
    def _validate_name(self, name: str) -> bool:
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        stripped = name.strip()
        if len(stripped) == 0 or any(c < 'a' for c in stripped.lower()):
            return False
        return True
    def verify_name(self, target_name: str) -> bool:
        try:
            names_in_db = self._load_data()
            logger.info(f"Searching for name '{target_name}'")
            if not isinstance(target_name, str):
                raise ValueError("Input must be a string")
            normalized_target = target_name.strip().lower()
            found_count = sum(1 for n in names_in_db if self._validate_name(n) and n.lower() == normalized_target)
            logger.info(f"Found {found_count} matching entries.")
            return len(names_in_db) > 0
        except Exception as e:
            logger.error(f"Verification failed with error: {e}")
            raise
if __name__ == '__main__':
    sample_data = [
        {"id": "1", "name": "Alice"},
        {"id": "2", "name": "Bob"},
        {"id": "3", "name": "Charlie"}
    ]
    with open('sample_names.json', 'w') as f:
        json.dump(sample_data, f)
    verifier = NameVerifier('sample_names.json')
    test_cases = [
        ("Alice"),
        ("bob"),
        ("Diana")
    ]
    for name in test_cases:
        try:
            result = verifier.verify_name(name)
            logger.info(f"Verification for '{name}': {'Success' if result else 'No match found'}")
        except Exception as e:
            logger.error(f"Error verifying '{name}': {e}")