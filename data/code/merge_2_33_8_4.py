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
    target_strings = ["grape", "fish", "rust"]
    for test_string in target_strings:
        result = check_string_in_lists(test_string, predefined_lists)
        logging.info(f"Target '{test_string}' found: {result}")
if __name__ == '__main__':
    main()