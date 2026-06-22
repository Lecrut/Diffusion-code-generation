def compare_dicts(dict1, dict2):
    common_pairs = {key: value for key, value in dict1.items() if key in dict2 and dict2[key] == value}
    return common_pairs

class DictComparator:
    def __init__(self, dict1, dict2):
        self.dict1 = dict1
        self.dict2 = dict2
    
    def get_common_pairs(self):
        return compare_dicts(self.dict1, self.dict2)

if __name__ == '__main__':
    sample_dict1 = {'a': 1, 'b': 2, 'c': 3}
    sample_dict2 = {'b': 2, 'c': 4, 'd': 5}
    
    comparator = DictComparator(sample_dict1, sample_dict2)
    common_pairs = comparator.get_common_pairs()
    
    print(f"Dictionary 1: {sample_dict1}")
    print(f"Dictionary 2: {sample_dict2}")
    print(f"Common key-value pairs: {common_pairs}")