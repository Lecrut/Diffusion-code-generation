def validate_key_exists(key, dict_list):
    if not isinstance(dict_list, list) or not all((isinstance(d, dict) for d in dict_list)):
        raise ValueError('dict_list must be a list of dictionaries')
    return any((key in d for d in dict_list))

class DictValidator:

    def __init__(self, dict_list):
        self.dict_list = dict_list

    def key_exists(self, key):
        return validate_key_exists(key, self.dict_list)

    def count_keys(self):
        return sum((1 for d in self.dict_list if self.key_exists(d)))
if __name__ == '__main__':
    validator = DictValidator([{'a': 1}, {'b': 2}, {'c': 3}, {'d': 4}, {'e': 5, 'f': 6}])
    print(validator.key_exists('c'))
    print(validator.count_keys())