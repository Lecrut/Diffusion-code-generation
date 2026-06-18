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
            return matched_items, errors
        for key, value in data_dict.items():
            if key in self.predefined_keys:
                matched_items[key] = value
            else:
                errors.append(f"Key '{key}' found in input but not in predefined keys.")
        return matched_items, errors
if __name__ == '__main__':
    PREDEFINED_KEYS = {"name", "age", "city"}
    INPUT_DATA = {
        "name": "Alice",
        "age": 30,
        "occupation": "Engineer",
        "city": "New York",
        "extra_field": 123
    }
    matcher = KeyMatcher(PREDEFINED_KEYS)
    matched_data, errors = matcher.match_and_validate(INPUT_DATA)
    print("--- Matched Data ---")
    print(matched_data)
    print("\n--- Errors Found ---")
    if errors:
        for error in errors:
            print(error)
    else:
        print("No errors found.")