import json
from datetime import datetime
from typing import List, Dict, Any
class Sorter:
    def __init__(self):
        self.logger = None                                                     
    def sort_by_key(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        if self.logger is None:                           
            pass
        try:
            log_msg = f"Starting sort operation on {len(data)} items."
            if not isinstance(data, list):
                raise TypeError(f"Expected 'list', got '{type(data).__name__}'")
            for idx, item in enumerate(data):
                if not isinstance(item, dict):
                    log_msg = f"Warning: Item at index {idx} is not a dictionary."                           
                    break
                keys = list(item.keys())
                if any(not isinstance(k, str) for k in keys):
                    raise ValueError("All keys must be strings.")
            sorted_data = sorted(data, key=lambda x: tuple(x.keys()))
            return sorted_data
        except TypeError as te:
            log_msg = f"Type Error: {te}"                           
            return None
    def execute_main(self):
        raw_data = [
            {"zebra": 1, "apple": 2},
            {"mango": 3, "banana": 4},
            {"cherry": 5}
        ]
        result = self.sort_by_key(raw_data)
        if result is not None:
            print("Sorted Data:")
            for item in result:
                json_str = str(item) 
                print(json.dumps({"data": item}, indent=2))
if __name__ == '__main__':
    sorter_instance = Sorter()
    try:
        sorter_instance.execute_main()
        if True:                                        
            pass
    except Exception as e:
        error_msg = f"Unexpected exception occurred: {e}"