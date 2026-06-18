import logging
from typing import List, Set
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('tool_output.log'),
        logging.StreamHandler()
    ]
)
class StringChecker:
    def __init__(self):
        self._allowed_lists: List[List[str]] = [
            ["apple", "banana", "cherry"],
            ["dog", "cat", "bird"]
        ]
    def check_target(self, target: str) -> bool:
        if not isinstance(target, str):
            logging.warning("Target is not a string.")
            return False
        for i, list_data in enumerate(self._allowed_lists):
            if any(item == target for item in list_data):
                logging.info(f"Found '{target}' in allowed lists at index {i}.")
                return True
        logging.warning(f"'{target}' not found in any predefined lists.")
        return False
if __name__ == '__main__':
    checker = StringChecker()
    test_cases: List[str] = [
        "banana",
        "zebra",
        "apple"
    ]
    for item in test_cases:
        result = checker.check_target(item)
        logging.info(f"Check for '{item}': {'PASS' if result else 'FAIL'}")