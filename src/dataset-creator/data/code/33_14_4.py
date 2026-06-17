import json
import logging
from pathlib import Path
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
class NameVerifier:
    def __init__(self, data_source_path: str):
        self.data_source_path = Path(data_source_path)
    def _load_data(self) -> dict[str, list]:
        if not self.data_source_path.exists():
            logger.error(f"Data source file {self.data_source_path} does not exist.")
            return {}
        try:
            with open(self.data_source_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            if isinstance(data, dict):
                names_data = data.get('names', [])
            else:
                logger.warning("Unexpected JSON structure. Treating root list as names.")
                names_data = [data]
            return {'valid_names': set(names_data)}
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse JSON file {self.data_source_path}: {e}")
            return {}
    def verify_name(self, name_to_check: str) -> bool:
        if not isinstance(name_to_check, str):
            raise ValueError("Name must be a string.")
        data = self._load_data()
        valid_names = data.get('valid_names', set())
        logger.info(f"Verifying presence of name '{name_to_check}' in database.")
        return name_to_check.lower() in [n.lower() for n in valid_names]
if __name__ == '__main__':
    sample_data_path = 'sample_database.json'
    verifier = NameVerifier(sample_data_path)
    test_cases = ['Alice', 'bob', 'Charlie123']
    for name in test_cases:
        try:
            result = verifier.verify_name(name)
            logger.info(f"Verification result for '{name}': {'Found' if result else 'Not Found'}")
        except ValueError as ve:
            logger.error(f"Validation error for input {ve}")