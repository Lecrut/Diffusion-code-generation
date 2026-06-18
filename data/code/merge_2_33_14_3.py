import json
import logging
from pathlib import Path
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
class NameVerifier:
    def __init__(self, data_source_type: str):
        self.data_source_type = data_source_type
        if data_source_type not in ['json_file', 'csv_file']:
            raise ValueError("Unsupported data source type")
    def _load_data(self) -> list[dict]:
        path_str = "sample_names.json" if self.data_source_type == 'json_file' else "names.csv"
        try:
            with open(path_str, 'r', encoding='utf-8') as f:
                data = json.load(f) if self.data_source_type == 'json_file' else list(csv.DictReader(open(path_str)))
            logger.info("Data loaded successfully")
            return data
        except FileNotFoundError:
            raise RuntimeError(f"File {path_str} not found")
    def verify_name(self, name: str) -> bool:
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        logger.info(f"Verifying name: '{name}'")
        try:
            data = self._load_data()
            for record in data:
                stored_name = record.get('name', '').strip().lower() if isinstance(record, dict) else str(record).strip().lower()
                if name.strip().lower() == stored_name:
                    logger.info(f"Name '{name}' found")
                    return True
            logger.warning(f"Name '{name}' not found in database")
            return False
        except Exception as e:
            logger.error(f"Error during verification: {e}")
            raise
if __name__ == '__main__':
    verifier = NameVerifier('json_file')
    sample_names = [
        "Alice",
        "bob",
        "Charlie123",
        "UnknownUser"
    ]
    for name in sample_names:
        try:
            result = verifier.verify_name(name)
            print(f"{name}: {'Verified' if result else 'Not Found'}")
        except Exception as e:
            logger.error(f"Error verifying {name}: {e}")