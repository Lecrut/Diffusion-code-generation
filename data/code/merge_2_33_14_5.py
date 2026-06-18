import json
import logging
from pathlib import Path
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
class NameVerifier:
    def __init__(self, db_path):
        self.db_path = Path(db_path)
    def validate_input(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string.")
        if len(name.strip()) == 0:
            raise ValueError("Name cannot be empty.")
        return True
    def load_data(self):
        try:
            with open(self.db_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            if not isinstance(data, list):
                raise ValueError("Database must contain a list of strings.")
            return set(name.strip() for name in data if isinstance(name, str))
        except FileNotFoundError:
            logger.warning(f"File {self.db_path} not found. Using empty dataset.")
            return set()
    def verify_name(self, target_name):
        try:
            self.validate_input(target_name)
            data = self.load_data()
            logger.info(f"Verifying presence of '{target_name}'")
            is_present = target_name.lower() in [n.strip().lower() for n in data]
            if is_present:
                logger.info("Name found.")
            else:
                logger.warning("Name not found.")
        except ValueError as ve:
            logger.error(f"Input validation failed: {ve}")
            return False
        return True
if __name__ == '__main__':
    db_file = "sample_names.json"
    target_name_to_check = "Alice"
    verifier = NameVerifier(db_file)
    result = verifier.verify_name(target_name_to_check)
    if result:
        print(f"\nVerification Result for '{target_name_to_check}': PRESENT")
    else:
        print(f"\nVerification Result for '{target_name_to_check}': ABSENT or INVALID INPUT")