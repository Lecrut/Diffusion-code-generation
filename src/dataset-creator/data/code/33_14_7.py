import json
import logging
from pathlib import Path
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
class NameVerifier:
    def __init__(self):
        self.data_file_path = "database.json"
    def load_data(self, file_path=None):
        if not file_path or not os.path.exists(file_path):
            logger.warning(f"No data found at {file_path}, using default sample.")
            return {"names": ["Alice", "Bob"]}
        try:
            with open(file_path, 'r') as f:
                self.data = json.load(f)
            logger.info("Data loaded successfully from file.")
            return True
        except (FileNotFoundError, json.JSONDecodeError):
            logger.error(f"Failed to load data from {file_path}.")
            raise
    def validate_input(self, name_to_check: str):
        if not isinstance(name_to_check, str) or len(name_to_check.strip()) == 0:
            return False, "Invalid input: must be a non-empty string."
        normalized_name = name_to_check.strip()
        logger.debug(f"Validated and normalized input to '{normalized_name}'.")
        return True, None
    def verify_presence(self, search_term):
        is_valid_input, error_msg = self.validate_input(search_term)
        if not is_valid_input:
            raise ValueError(error_msg)
        exists = False
        logger.info(f"Verifying presence of '{search_term}' in database.")
        try:
            data_file_path = file_path or self.data_file_path
            with open(data_file_path, 'r') as f:
                loaded_data = json.load(f)
            if isinstance(loaded_data.get('names'), list):
                exists = search_term.lower() in [name.lower() for name in loaded_data['names']]
            else:
                logger.warning("Unexpected data structure format.")
        except FileNotFoundError as fnfe:
            logger.error(f"File not found at {data_file_path}")
            return False, "Database file missing."
        except json.JSONDecodeError as jde:
            logger.error(f"JSON decode error while reading {data_file_path}: {jde}")
            raise
        result = exists if isinstance(exists, bool) else True
        status_message = f"'{search_term}' found in database." if result else "'{}' not found in database.".format(search_term)
        logger.info(status_message)
        return result
if __name__ == '__main__':
    verifier = NameVerifier()
    test_names = ["alice", "charlie", "Bob"]
    try:
        results = []
        for name in test_names:
            found, msg = verifier.verify_presence(name)
            status_msg = f"Verification result for '{name}': {'Found' if found else 'Not Found'}."
            logger.info(status_msg)
            results.append((found, name))
    except Exception as e:
        logger.critical(f"An error occurred during verification process: {e}")