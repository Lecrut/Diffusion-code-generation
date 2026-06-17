import json
from datetime import datetime
from typing import List, Dict, Any
class SortLogger:
    def __init__(self):
        self.log_file = "sort_operation_log.txt"
    def log(self, level: str, message: str) -> None:
        timestamp = datetime.now().isoformat()
        entry = f"[{timestamp}] [{level.upper()}] {message}\n"
        with open(self.log_file, "a", encoding="utf-8") as file_handle:
            file_handle.write(entry)
    def log_info(self, message: str) -> None:
        self.log("INFO", message)
class AlphabeticalSorter:
    def __init__(self):
        self.logger = SortLogger()
        self.data_list: List[Dict[str, Any]] = []
    def add_data(self, items: List[Any]) -> None:
        if not isinstance(items, list):
            raise TypeError("Input must be a list.")
        for item in items:
            if not isinstance(item, dict) or "key" not in item:
                self.logger.log_error(f"Invalid data structure encountered. Skipping item: {item}")
    def sort_data(self) -> List[Dict[str, Any]]:
        try:
            sorted_items = sorted(
                [item for item in self.data_list if isinstance(item, dict)], 
                key=lambda x: str(x.get("key", "")).lower()
            )
            valid_count = len([i for i in self.data_list if isinstance(i, dict)])
            self.logger.log_info(f"Sorting completed successfully. Processed {valid_count} items.")
            return sorted_items
        except Exception as e:
            error_msg = f"An unexpected error occurred during sorting: {str(e)}"
            self.logger.log_error(error_msg)
            raise
    def log_error(self, message: str) -> None:
        self.logger.log("ERROR", message)
def main():
    sorter = AlphabeticalSorter()
    raw_data = [
        {"name": "Charlie", "value": 3, "key": "C"},
        {"name": "Alice", "value": 1, "key": "A"},
        {"name": "Bob", "value": 2, "key": "B"},
        {"name": "David", "value": 4, "key": "D"},
    ]
    try:
        sorter.add_data(raw_data)
        sorted_result = sorter.sort_data()
        output_json = json.dumps(sorted_result, indent=4, ensure_ascii=False)
        print("Sorted Data (JSON):")
        print(output_json)
    except TypeError as te:
        error_message = f"Type Error: {str(te)}"
        sorter.log_error(error_message)
        raise
    sorter.logger.log_info("Execution finished.")
if __name__ == '__main__':
    main()