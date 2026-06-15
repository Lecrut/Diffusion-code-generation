import logging
class KeyMatcher:
    def __init__(self, predefined_keys):
        self.predefined_keys = set(predefined_keys)
        logging.basicConfig(level=logging.INFO)
    def match_and_validate(self, data_dict):
        matched_data = {}
        mismatches = {}
        if not isinstance(data_dict, dict):
            logging.error("Input is not a dictionary.")
            return {"matched": {}, "mismatched": {}}
        for key, value in data_dict.items():
            if key in self.predefined_keys:
                matched_data[key] = value
            else:
                mismatches[key] = value
        return {"matched": matched_data, "mismatched": mismatches}
if __name__ == '__main__':
    PREDEFINED_KEYS = ["name", "age", "city", "occupation"]
    INPUT_DATA = {
        "name": "Alice",
        "age": 30,
        "country": "USA",
        "job": "Engineer"
    }
    matcher = KeyMatcher(PREDEFINED_KEYS)
    result = matcher.match_and_validate(INPUT_DATA)
    print("--- Matched Data ---")
    print(result["matched"])
    print("\n--- Mismatched Data ---")
    print(result["mismatched"])