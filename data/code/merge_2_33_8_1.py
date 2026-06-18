import logging
from typing import List, Optional
def setup_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s | %(levelname)-8s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
def check_string_in_lists(target: str, lists: List[List[str]]) -> bool:
    for list_item in lists:
        if target in list_item:
            return True
    return False
if __name__ == '__main__':
    setup_logging()
    sample_lists = [
        ["apple", "banana", "cherry"],
        ["dog", "cat", "bird"]
    ]
    test_cases = [
        ("apple", True),
        ("grape", False),
        ("dog", True)
    ]
    for target, expected in test_cases:
        result = check_string_in_lists(target, sample_lists)
        status = "PASS" if result == expected else "FAIL"
        logging.info(f"[{status}] Target '{target}' found: {result}")