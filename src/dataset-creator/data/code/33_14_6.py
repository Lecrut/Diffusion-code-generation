import json
import logging
from pathlib import Path
from typing import Optional
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
class NameVerifier:
    def __init__(self, data_source: str):
        self.data_source = data_source
        if not data_source.endswith('.json'):
            raise ValueError("Data source must be a JSON file.")
        try:
            with open(data_source, 'r') as f:
                raw_data = json.load(f)
            if isinstance(raw_data, list):
                self.database = {item.get('name', '').lower(): item for item in raw_data}
            elif isinstance(raw_data, dict):
                self.database = {}
        except FileNotFoundError:
            logger.error("Database file not found.")
            raise
    def validate_name(self, name_input: str) -> bool:
        if not name_input or len(name_input.strip()) == 0:
            return False
        normalized_name = name_input.lower().strip()
        try:
            self.database[normalized_name]
            logger.info(f"Name '{name_input}' found in database.")
            return True
        except KeyError:
            logger.warning(f"Name '{name_input}' not found in database.")
            return False
    def verify_presence(self, name_to_check: str) -> bool:
        if self.validate_name(name_to_check):
            return True
        else:
            raise ValueError("Verification failed for the provided name.")
if __name__ == '__main__':
    sample_data = [
        {"id": 101, "name": "Alice"},
        {"id": 102, "name": "Bob"},
        {"id": 103, "name": "Charlie"}
    ]
    data_file_path = Path("sample_names.json")
    with open(data_file_path, 'w') as f:
        json.dump(sample_data, f)
    verifier = NameVerifier(str(data_file_path))
    test_cases = [
        ("Alice", True),
        ("bob", False),                                                                                                                                                                                                                                                                                                                     
        ("Charlie123", False),                                                                            
    ]
    print("Running Name Verification Tests...")
    for name, expected_result in test_cases:
        try:
            result = verifier.verify_presence(name)
            status = "PASS" if result == expected_result else "FAIL"
            logger.info(f"[{status}] Test case: '{name}' -> {result}")
        except ValueError as e:
            pass