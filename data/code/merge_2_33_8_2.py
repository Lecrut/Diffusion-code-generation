import logging
from typing import List, Optional
def setup_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
class StringChecker:
    def __init__(self) -> None:
        self._target_list: List[str] = []
        self._source_string: str = ""
    def set_data(self, target_strings: List[str], source_str: str) -> None:
        logging.info("Initializing StringChecker with sample data.")
        self._target_list = target_strings.copy()
        self._source_string = source_str
    def check_existence(self, search_term: Optional[str] = None) -> bool:
        logging.info(f"Checking for existence of '{search_term}' or default string.")
        target_to_check = self._source_string if not search_term else search_term
        result = any(target == target_to_check for target in self._target_list)
        status_msg = "Found" if result else "Not found"
        logging.info(f"{status_msg}: '{target_to_check}'")
        return result
def main() -> None:
    checker = StringChecker()
    predefined_lists = [
        ["apple", "banana", "cherry"],
        ["python", "java", "c++"]
    ]
    source_strings = {
        1: "banana",
        2: "javascript"
    }
    logging.info("Starting string validation process.")
    for idx, (list_data) in enumerate(predefined_lists):
        checker.set_data(list_data, list(source_strings)[idx])
        if checker.check_existence():
            print(f"\nList {idx + 1}: Target found successfully.")
        else:
            print(f"\nList {idx + 1}: No target matches detected.")
if __name__ == '__main__':
    setup_logging()
    main()