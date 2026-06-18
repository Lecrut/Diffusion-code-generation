import logging
class KeyMatcher:
    def __init__(self, predefined_keys):
        self.predefined_keys = set(predefined_keys)
        logging.basicConfig(level=logging.INFO)
    def match_dictionary(self, data_dict):
        matched_items = {}
        for key, value in data_dict.items():
            if key in self.predefined_keys:
                matched_items[key] = value
            else:
                logging.warning(f"Key '{key}' from input dictionary not found in predefined keys.")
        return matched_items
if __name__ == '__main__':
    predefined = {"name", "age", "city"}
    input_data_valid = {"name": "Alice", "age": 30, "extra_field": "ignore"}
    input_data_mismatch = {"name": "Bob", "occupation": "Engineer", "city": "New York"}
    input_data_empty = {}
    input_data_invalid = {"name": 123}
    matcher = KeyMatcher(predefined)
    print("--- Testing Valid Input ---")
    result_valid = matcher.match_dictionary(input_data_valid)
    print(f"Input: {input_data_valid}")
    print(f"Predefined Keys: {predefined}")
    print(f"Matched Result: {result_valid}\n")
    print("--- Testing Mismatched Input ---")
    result_mismatch = matcher.match_dictionary(input_data_mismatch)
    print(f"Input: {input_data_mismatch}")
    print(f"Predefined Keys: {predefined}")
    print(f"Matched Result: {result_mismatch}\n")
    print("--- Testing Empty Input ---")
    result_empty = matcher.match_dictionary(input_data_empty)
    print(f"Input: {input_data_empty}")
    print(f"Predefined Keys: {predefined}")
    print(f"Matched Result: {result_empty}\n")
    print("--- Testing Input with Invalid Data Types (Graceful Handling) ---")
    result_invalid = matcher.match_dictionary(input_data_invalid)
    print(f"Input: {input_data_invalid}")
    print(f"Predefined Keys: {predefined}")
    print(f"Matched Result: {result_invalid}\n")