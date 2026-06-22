class KeyEqualityChecker:
    def __init__(self, input_dict):
        self.input_dict = input_dict

    @staticmethod
    def validate_keys(input_dict, key1, key2):
        if not isinstance(input_dict, dict):
            raise ValueError("Input must be a dictionary.")
        if key1 not in input_dict or key2 not in input_dict:
            raise KeyError(f"One or both keys ({key1}, {key2}) are missing from the dictionary.")

    def check_keys_identical(self, key1, key2):
        self.validate_keys(self.input_dict, key1, key2)
        return {key1: self.input_dict[key1] == self.input_dict.get(key2)}

if __name__ == '__main__':
    sample_dict = {'u': 3, 'v': 9, 'w': 3}
    checker = KeyEqualityChecker(sample_dict)
    try:
        result = checker.check_keys_identical('u', 'w')
        print(result)
    except (ValueError, KeyError) as e:
        print(e)