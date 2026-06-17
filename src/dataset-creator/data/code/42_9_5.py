import json
from datetime import datetime
from typing import List, Dict, Any
class SortLogger:
    def __init__(self):
        self.log_file = "sort_operation_log.txt"
    def log(self, level: str, message: str) -> None:
        timestamp = datetime.now().isoformat()
        entry = f"[{timestamp}] [{level.upper()}] {message}\n"
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(entry)
    def log_info(self, message: str) -> None:
        self.log("INFO", message)
class AlphabeticalSorter:
    def __init__(self):
        self.logger = SortLogger()
        self.data_list: List[Dict[str, Any]] = []
    def validate_input(self, data: List[Any]) -> bool:
        if not isinstance(data, list):
            raise TypeError("Input must be a list.")
        for item in data:
            if not isinstance(item, dict) or "name" not in item:
                return False
        self.logger.log_info(f"Validation passed. Input size: {len(data)}")
        return True
    def sort_data(self, reverse_order: bool = False) -> List[Dict[str, Any]]:
        if not isinstance(reverse_order, bool):
            raise ValueError("reverse_order must be a boolean.")
        try:
            self.logger.log_info(f"Starting alphabetical sort. Reverse order: {reverse_order}")
            sorted_data = [item.copy() for item in self.data_list]
            if not reverse_order:
                sorted_data.sort(key=lambda x: str(x.get("name", "")).lower())
            else:
                sorted_data.sort(key=lambda x: str(x.get("name", "")).lower(), reverse=True)
            self.logger.log_info(f"Sorting completed successfully. Result size: {len(sorted_data)}")
        except Exception as e:
            error_msg = f"An unexpected error occurred during sorting: {str(e)}"
            self.logger.log_error(error_msg)
            raise RuntimeError("Sort operation failed.") from e
    def log_error(self, message: str) -> None:
        timestamp = datetime.now().isoformat()
        entry = f"[{timestamp}] [ERROR] {message}\n"
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(entry)
def main():
    raw_data = [
        {"name": "Charlie", "value": 3},
        {"name": "Alice", "value": 1},
        {"name": "Bob", "value": 2}
    ]
    try:
        sorter = AlphabeticalSorter()
        if not sorter.validate_input(raw_data):
            raise ValueError("Input data failed validation checks.")
        sorted_result = sorter.sort_data(reverse_order=False)
        print("\nSorted Data (Ascending):")
        for item in sorted_result:
            print(f"  {item['name']}: {item['value']}")
    except Exception as e:
        if isinstance(e, RuntimeError) and "Sort operation failed" not in str(e):
            raise
        print("\nAn unexpected critical error occurred.")
if __name__ == '__main__':
    main()