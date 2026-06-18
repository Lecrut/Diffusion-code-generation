import json
import logging
from pathlib import Path
from typing import Optional, List
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
class NameVerifier:
    def __init__(self, data_source: str):
        self.data_source = data_source
        self._data_cache: dict[str, bool] = {}
    def _load_data(self) -> List[dict]:
        if not Path(self.data_source).exists():
            logger.error(f"Data source {self.data_source} does not exist.")
            return []
        try:
            with open(self.data_source, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if isinstance(data, list):
                    self._data_cache.clear()
                    for item in data:
                        name = str(item.get('name')) or ''
                        self._data_cache[name] = True
                else:
                    logger.warning("Data source is not a JSON array.")
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse {self.data_source}: {e}")
        return []
    def verify_name(self, name_to_check: str) -> bool:
        if not isinstance(name_to_check, str):
            raise ValueError("Name must be a string.")
        normalized_name = name_to_check.strip().lower()
        logger.info(f"Verifying presence of '{name_to_check}'")
        return self._data_cache.get(normalized_name, False)
def main():
    sample_data = [
        {"id": 101, "name": "Alice"},
        {"id": 102, "name": "Bob"},
        {"id": 103, "name": "Charlie"}
    ]
    temp_file_path = Path("temp_names.json")
    with open(temp_file_path, 'w', encoding='utf-8') as f:
        json.dump(sample_data, f)
    verifier = NameVerifier(str(temp_file_path))
    test_cases = [
        "Alice",
        "alice",                         
        "Bob",
        "Diana",              
        ""                                
    ]
    for name in test_cases:
        try:
            result = verifier.verify_name(name)
            logger.info(f"Result for '{name}': {'Found' if result else 'Not Found'}")
        except ValueError as e:
            logger.error(f"Validation error for input {e}")
if __name__ == '__main__':
    main()