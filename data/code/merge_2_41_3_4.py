import json
import sys
from typing import Any, Dict, List
class DataCounter:
    def __init__(self):
        self.error_log = []
    def _log_error(self, message: str) -> None:
        error_entry = {"level": "ERROR", "message": message}
        print(json.dumps(error_entry), file=sys.stderr)
        self.error_log.append(error_entry)
    def count_items(self, data: Any) -> Dict[str, int]:
        counts = {
            'strings': 0,
            'integers': 0,
            'objects': 0,
            'others': 0
        }
        if not isinstance(data, list):
            self._log_error(f"Input must be a list. Received: {type(data).__name__}")
            return counts
        for index, item in enumerate(data):
            try:
                string_count = False
                int_count = False
                object_count = False
                if isinstance(item, str) and not (isinstance(item, bool)):
                    string_count = True
                elif isinstance(item, int) and not (isinstance(item, bool)):
                    int_count = True
                else:
                    object_count = True
                if string_count:
                    counts['strings'] += 1
                elif int_count:
                    counts['integers'] += 1
                elif object_count:
                    counts['objects'] += 1
                else:
                    if not isinstance(item, (str, int)):
                        counts['others'] += 1
            except Exception as e:
                self._log_error(f"Error processing item at index {index}: {str(e)}")
        return counts
if __name__ == '__main__':
    counter = DataCounter()
    sample_data = [
        "apple",
        42,
        {"key": "value"},
        "banana",
        True,                                                                                                         
        None,
        100.5, 
        [1, 2],
    ]
    result = counter.count_items(sample_data)
    print("Item Counts Report:")
    for category, count in result.items():
        print(f"  {category}: {count}")