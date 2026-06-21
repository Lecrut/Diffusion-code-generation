class DictKeyValidator:
    def __init__(self, dict_list):
        if not isinstance(dict_list, list) or not all(isinstance(d, dict) for d in dict_list):
            raise ValueError("dict_list must be a list of dictionaries")
        self.dict_list = dict_list
    
    def validate_key(self, key):
        return any(key in d for d in self.dict_list)

if __name__ == '__main__':
    validator = DictKeyValidator([{'a': 1}, {'b': 2}, {'c': 3}])
    print(validator.validate_key('b'))
    print(validator.validate_key('d'))