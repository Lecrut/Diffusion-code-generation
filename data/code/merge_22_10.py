import logging
class KeyMatcher:
    def __init__(self, predefined_keys):
        self.predefined_keys = set(predefined_keys)
        logging.basicConfig(level=logging.INFO)
    def match_dictionary(self, data_dict):
        matched_data = {}
        for key, value in data_dict.items():
            if key in self.predefined_keys:
                matched_data[key] = value
            else:
                logging.warning(f"Key '{key}' from input dictionary not found in predefined keys.")
                matched_data[f"unmatched_{key}"] = value
        return matched_data
if __name__ == '__main__':
    predefined = {"name", "age", "city"}
    input_data = {
        "name": "Alice",
        "age": 30,
        "occupation": "Engineer",
        "city": "New York",
        "extra_field": 123
    }
    matcher = KeyMatcher(predefined)
    result = matcher.match_dictionary(input_data)
    print(result)