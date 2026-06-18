import logging
from typing import List, Optional
def setup_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s | %(levelname)-8s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
def check_string_in_lists(target: str, lists: List[List[str]]) -> bool:
    for index, sublist in enumerate(lists):
        logging.debug(f"Checking list {index}: {sublist}")
        if target in sublist:
            return True
    return False
def main() -> None:
    setup_logging()
    predefined_lists = [
        ["apple", "banana", "cherry"],
        ["dog", "cat", "bird"],
        ["python", "java", "c++"]
    ]
    target_strings = ["banana", "zebra", "javascript"]
    for test_string in target_strings:
        logging.info(f"Checking if '{test_string}' exists in predefined lists.")
        result = check_string_in_lists(test_string, predefined_lists)
        status_message = f"'{test_string}' FOUND" if result else f"'{test_string}' NOT FOUND"
        logging.info(status_message)
if __name__ == '__main__':
    main()