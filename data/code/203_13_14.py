class DictComparator:
    def __init__(self, dict1, dict2):
        self.dict1 = dict1
        self.dict2 = dict2

    def compare(self):
        return all(key in self.dict2 and self.dict2[key] == value for key, value in self.dict1.items())

if __name__ == '__main__':
    sample_dict1 = {'a': 1, 'b': 2, 'c': 3}
    sample_dict2 = {'a': 1, 'b': 2, 'c': 4}
    comparator = DictComparator(sample_dict1, sample_dict2)
    result = comparator.compare()
    print(result)