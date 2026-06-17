import json
from datetime import datetime
class StringChecker:
    def __init__(self):
        self.target_strings = [
            "apple",
            "banana",
            "cherry"
        ]
        self.reference_lists = {
            "fruits": ["apple", "orange", "grape"],
            "colors": ["red", "blue", "green"]
        }
    def check_string(self, target: str) -> bool:
        return any(target in items for list_items in self.target_strings if isinstance(list_items, (list, tuple)) and item == target for item in list_items) or\
               any(item.lower() == target.lower() for sublist in self.reference_lists.values() for item in sublist)
    def log_operation(self, message: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"
        with open("check_log.txt", "a") as log_file:
            log_file.write(log_entry)
if __name__ == '__main__':
    checker_instance = StringChecker()
    test_cases = [
        {"target": "apple", "expected_result": True, "list_name": None},
        {"target": "mango", "expected_result": False, "list_name": None}
    ]
    for case in test_cases:
        result = checker_instance.check_string(case["target"])
        if result == case["expected_result"]:
            status_message = f"Test passed. '{case['target']}' correctly identified."
        else:
            status_message = f"Test failed. Expected {case['expected_result']}, got {result} for '{case['target']}.'"
        checker_instance.log_operation(status_message)