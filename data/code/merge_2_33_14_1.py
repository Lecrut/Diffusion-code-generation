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
            logger.error(f"Data source file '{self.data_source_path}' does not exist.")
            return []
        try:
            with open(self.data_source_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if isinstance(data, list):
                    return [item.get('name', '') for item in data]
                elif isinstance(data, dict):
                    return [data.get('names', [])]
        except (json.JSONDecodeError, IOError) as e:
            logger.error(f"Failed to load data from '{self.data_source_path}': {e}")
        return []
    def verify_name(self, name_to_check: str) -> bool:
        if not isinstance(name_to_check, str):
            raise ValueError("Name must be a string.")
        names = self._load_data()
        logger.info(f"Verifying presence of '{name_to_check}' in database.")
        return any(n.lower().strip() == name_to_check.lower().strip() for n in names)
if __name__ == '__main__':
    sample_names = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"}
    ]
    with open('sample_data.json', 'w') as f:
        json.dump(sample_names, f)
    verifier = NameVerifier('sample_data.json')
    test_cases = ["alice", "CHARLIE", "", None]
    for name in test_cases:
        try:
            result = verifier.verify_name(name) if isinstance(name, str) else False
            logger.info(f"Name '{name}' present: {result}")
        except Exception as e:
            logger.error(f"Error verifying name '{name}': {e}")