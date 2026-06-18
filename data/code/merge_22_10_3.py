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
    predefined_keys = ["name", "age", "city", "occupation"]
    input_data_1 = {
        "name": "Alice",
        "age": 30,
        "country": "USA",
        "occupation": "Engineer"
    }
    input_data_2 = {
        "name": "Bob",
        "city": "New York",
        "job": "Developer"
    }
    invalid_input = [1, 2, 3]
    matcher = KeyMatcher(predefined_keys)
    print("--- Matching Input Data 1 ---")
    result_1 = matcher.match_dictionary(input_data_1)
    print(result_1)
    print("\n--- Matching Input Data 2 (Mismatches Handled) ---")
    result_2 = matcher.match_dictionary(input_data_2)
    print(result_2)
    print("\n--- Handling Invalid Input Type ---")
    result_invalid = matcher.match_dictionary(invalid_input)
    print(result_invalid)