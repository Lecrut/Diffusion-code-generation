import json
import logging
from pathlib import Path
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
class NameVerifier:
    def __init__(self, data_path: str):
        self.data_path = Path(data_path)
    def _validate_input(self, name: str) -> bool:
        if not isinstance(name, str):
            logger.error("Input must be a string.")
            return False
        stripped_name = name.strip()
        if len(stripped_name) == 0:
            logger.warning("Empty input provided.")
            return True
        for char in stripped_name:
            if not (char.isalpha() or char.isspace()):
                logger.error(f"Invalid character '{char}' found in name.")
                return False
        return True
    def _load_data(self) -> dict:
        try:
            with open(self.data_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            if not isinstance(data, list):
                logger.error("Data file must contain a JSON array.")
                return {}
            valid_names = []
            for item in data:
                if isinstance(item, dict) and 'name' in item:
                    name_val = str(item['name']).strip()
                    if len(name_val) > 0:
                        valid_names.append(name_val)
            logger.info(f"Loaded {len(valid_names)} names from database.")
            return {'names': set(valid_names)}
        except FileNotFoundError:
            logger.warning(f"File '{self.data_path}' not found. Using empty dataset.")
            return {}
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse JSON file: {e}")
            return {}
    def verify_name(self, name: str) -> bool:
        if not self._validate_input(name):
            return False
        loaded_data = self._load_data()
        names_set = loaded_data.get('names', set())
        logger.info(f"Verifying presence of '{name}' in database.")
        is_present = name.lower().strip() in [n.lower().strip() for n in names_set]
        if is_present:
            logger.info("Name found successfully.")
        else:
            logger.warning("Name not found in the provided dataset.")
        return is_present
if __name__ == '__main__':
    sample_data = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob Smith"}
    ]
    with open('sample_names.json', 'w') as f:
        json.dump(sample_data, f)
    verifier = NameVerifier(data_path='sample_names.json')
    test_cases = [
        ("alice", True),
        ("bob smith", True),
        ("charlie", False),
        (12345, False),
        ("  john doe  ", True)
    ]
    for input_name, expected_result in test_cases:
        result = verifier.verify_name(input_name)
        status = "PASS" if result == expected_result else "FAIL"
        logger.info(f"Test '{input_name}': {status}")