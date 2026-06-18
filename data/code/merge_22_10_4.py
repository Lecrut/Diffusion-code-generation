import logging
class KeyMatcher:
    def __init__(self, predefined_keys):
        self.predefined_keys = set(predefined_keys)
        logging.basicConfig(level=logging.INFO)
    def match_dictionary(self, data_dict):
        matched_items = {}
        if not isinstance(data_dict, dict):
            logging.error("Input is not a dictionary.")
            return matched_items
        for key, value in data_dict.items():
            if key in self.predefined_keys:
                matched_items[key] = value
            else:
                logging.warning(f"Key '{key}' from input dictionary not found in predefined keys.")
                matched_items[key] = None
        return matched_items
if __name__ == '__main__':
    predefined = {"name", "age", "city"}
    input_data_good = {"name": "Alice", "age": 30, "extra_field": "ignore"}
    input_data_mismatch = {"name": "Bob", "occupation": "Engineer", "city": "New York"}
    input_data_empty = {}
    input_data_invalid = [1, 2, 3]
    matcher = KeyMatcher(predefined)
    print("--- Test Case 1: Good Match ---")
    result1 = matcher.match_dictionary(input_data_good)
    print(f"Input: {input_data_good}")
    print(f"Result: {result1}\n")
    print("--- Test Case 2: Mismatched Keys ---")
    result2 = matcher.match_dictionary(input_data_mismatch)
    print(f"Input: {input_data_mismatch}")
    print(f"Result: {result2}\n")
    print("--- Test Case 3: Empty Dictionary ---")
    result3 = matcher.match_dictionary(input_data_empty)
    print(f"Input: {input_data_empty}")
    print(f"Result: {result3}\n")
    print("--- Test Case 4: Invalid Input Type (List) ---")
    result4 = matcher.match_dictionary(input_data_invalid)
    print(f"Input: {input_data_invalid}")
    print(f"Result: {result4}\n")