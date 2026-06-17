import logging
from typing import List, Optional
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
class StringChecker:
    def __init__(self):
        self.target_list = ["apple", "banana", "cherry"]
        self.user_input_list = ["grape", "fig", "date"]
    def check_target_in_lists(self, target_string: str) -> bool:
        if not isinstance(target_string, str):
            logging.error("Invalid input type. Expected string.")
            return False
        found = any(item == target_string for item in self.target_list or self.user_input_list)
        if found:
            logging.info(f"Target '{target_string}' found in predefined lists.")
        else:
            logging.warning(f"Target '{target_string}' not found in predefined lists.")
        return found
def run_checks():
    checker = StringChecker()
    test_cases = [
        "apple",
        "mango",
        "cherry"
    ]
    for item in test_cases:
        result = checker.check_target_in_lists(item)
        logging.info(f"Check completed for '{item}': {'Success' if result else 'Failed'}")
if __name__ == '__main__':
    run_checks()