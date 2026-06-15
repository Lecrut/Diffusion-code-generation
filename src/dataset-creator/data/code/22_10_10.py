import logging
class KeyMatcher:
    def __init__(self, predefined_keys):
        self.predefined_keys = set(predefined_keys)
        logging.basicConfig(level=logging.INFO)
    def match_and_validate(self, data_dict):
        results = {}
        if not isinstance(data_dict, dict):
            logging.error("Input must be a dictionary.")
            return results
        for key, value in data_dict.items():
            if key in self.predefined_keys:
                results[key] = value
            else:
                logging.warning(f"Key '{key}' from input data not found in predefined keys.")
                results[key] = None
        return results
if __name__ == '__main__':
    predefined = {"name", "age", "city"}
    matcher = KeyMatcher(predefined)
    sample_data_1 = {
        "name": "Alice",
        "age": 30,
        "occupation": "Engineer"
    }
    sample_data_2 = {
        "name": "Bob",
        "city": "New York",
        "extra_field": 100
    }
    sample_data_3 = {
        "age": 25,
        "job": "Developer"
    }
    print("--- Matching Sample Data 1 ---")
    result_1 = matcher.match_and_validate(sample_data_1)
    print(result_1)
    print("\n--- Matching Sample Data 2 ---")
    result_2 = matcher.match_and_validate(sample_data_2)
    print(result_2)
    print("\n--- Matching Sample Data 3 ---")
    result_3 = matcher.match_and_validate(sample_data_3)
    print(result_3)