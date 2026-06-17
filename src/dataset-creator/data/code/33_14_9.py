import json
import logging
from pathlib import Path
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
class NameVerifier:
    def __init__(self, data_source_path: str):
        self.data_source_path = Path(data_source_path)
        if not self.data_source_path.exists():
            raise FileNotFoundError(f"Data source '{data_source_path}' does not exist.")
        try:
            with open(self.data_source_path, 'r', encoding='utf-8') as f:
                raw_data = json.load(f)
            if not isinstance(raw_data, list):
                raise ValueError("Data source must contain a JSON array.")
            for item in raw_data:
                if not isinstance(item, str):
                    raise TypeError(f"Invalid name type found at index {raw_data.index(item)}. Expected string.")
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse JSON data from '{data_source_path}': {e}")
            raise
        self.names = raw_data
    def verify_name(self, target_name: str) -> bool:
        if not isinstance(target_name, str):
            logger.error(f"Invalid input type '{type(target_name)}' for verification. Expected string.")
            return False
        if not target_name.strip():
            logger.warning("Empty name provided during verification.")
        normalized_target = target_name.strip()
        found_index = next((i for i, item in enumerate(self.names) 
                          if self._normalize_string(item).lower() == normalized_target.lower()), -1)
        logger.info(f"Verification result: '{normalized_target}' {'found' if found_index != -1 else 'not found'} at index {found_index}.")
        return found_index != -1
    def _normalize_string(self, s: str) -> str:
        return " ".join(s.split())
if __name__ == '__main__':
    try:
        verifier = NameVerifier("sample_names.json")
        test_cases = [
            "alice",                                             
            "BOB",                          
            "david",                   
            "",                                    
            None                                                                                   
        ]
        for name in test_cases:
            result = verifier.verify_name(name)
    except FileNotFoundError as e:
        logger.error(f"Setup error: {e}")
        print("Please ensure 'sample_names.json' exists with a valid JSON array of strings.")
    except Exception as e:
        logger.critical(f"Unexpected error occurred: {e}", exc_info=True)