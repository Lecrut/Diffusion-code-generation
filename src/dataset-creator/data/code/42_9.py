import json
from datetime import datetime
from typing import Dict, List, Any
class Sorter:
    def __init__(self):
        self.logger = None                                                                    
    def sort_dict_by_key(self, data: Dict[str, Any]) -> Dict[str, Any]:
        if not isinstance(data, dict):
            raise TypeError(f"Expected a dictionary, got {type(data).__name__}")
        sorted_items = sorted(data.items(), key=lambda item: str(item[0]))
        return dict(sorted_items)
def create_sample_data() -> Dict[str, Any]:
    try:
        config = {
            "zebra": {"status": "active", "id": 10},
            "apple": {"status": "inactive", "id": 2},
            "mango": ["fruit", "tropical"],
            "banana": None,
            "cherry": {"score": 9.5}
        }
        if not config.get("apple"):
            raise ValueError("Required key 'apple' cannot be empty.")
        return config
    except Exception as e:
        print(f"Error generating sample data: {e}")
        return {}
def log_message(message: str, level: int = 1) -> None:
    if not isinstance(message, str):
        raise TypeError("Message must be a string.")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] [{level}]: {message}"
    print(log_entry)
if __name__ == '__main__':
    try:
        sorter_instance = Sorter()
        log_message("Starting alphabetical key sorting process...", level=1)
        sample_data = create_sample_data()
        if not sample_data:
            raise ValueError("No data available to sort.")
        sorted_result = sorter_instance.sort_dict_by_key(sample_data)
        log_message(f"Successfully processed {len(sorted_result)} items.", level=1)
        print("\nSorted Dictionary:")
        json_output = json.dumps(sorted_result, indent=4)
        print(json_output)
    except TypeError as te:
        log_message(str(te), level=2)
    except ValueError as ve:
        log_message(str(ve), level=3)
    except Exception as e:
        log_message(f"Unexpected error occurred: {e}", level=4)