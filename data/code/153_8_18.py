class DictKeyValidator:
    @staticmethod
    def validate_key_exists(key, dict_list):
        if not isinstance(dict_list, list) or not all(isinstance(d, dict) for d in dict_list):
            raise ValueError("dict_list must be a list of dictionaries")
        return any(key in d for d in dict_list)

if __name__ == '__main__':
    sample_dicts = [{'a': 1}, {'b': 2}, {'c': 3}]
    key_to_check = 'b'
    validator = DictKeyValidator()
    print(validator.validate_key_exists(key_to_check, sample_dicts))