import logging
class KeyMatcher:
    def __init__(self, predefined_keys):
        self.predefined_keys = set(predefined_keys)
        logging.basicConfig(level=logging.INFO)
    def match_and_validate(self, data_dict):
        matched_items = {}
        errors = []
        if not isinstance(data_dict, dict):
            errors.append("Input must be a dictionary.")
            return None, errors
        for key, value in data_dict.items():
            if key in self.predefined_keys:
                matched_items[key] = value
            else:
                errors.append(f"Key '{key}' found in data but not in predefined keys.")
        if errors:
            logging.warning("Matching completed with errors:")
            for error in errors:
                logging.warning(error)
        return matched_items, errors
if __name__ == '__main__':
    predefined = {"name", "age", "city"}
    data1 = {"name": "Alice", "age": 30, "occupation": "Engineer"}
    data2 = {"name": "Bob", "job": "Developer", "city": "New York"}
    data3 = {"name": "Charlie", "extra_field": 100}
    data4 = {"name": "David", "age": "twenty"}
    matcher = KeyMatcher(predefined)
    print("--- Testing Data 1 ---")
    result1, errors1 = matcher.match_and_validate(data1)
    print("Matched Data:", result1)
    print("Errors:", errors1)
    print("\n--- Testing Data 2 ---")
    result2, errors2 = matcher.match_and_validate(data2)
    print("Matched Data:", result2)
    print("Errors:", errors2)
    print("\n--- Testing Data 3 ---")
    result3, errors3 = matcher.match_and_validate(data3)
    print("Matched Data:", result3)
    print("Errors:", errors3)
    print("\n--- Testing Data 4 (Value Type Check Implicitly Handled by Matching) ---")
    result4, errors4 = matcher.match_and_validate(data4)
    print("Matched Data:", result4)
    print("Errors:", errors4)