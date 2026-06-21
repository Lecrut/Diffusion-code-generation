class DictComparator:
    def __init__(self, dict1: dict, dict2: dict):
        self.dict1 = dict1
        self.dict2 = dict2

    def are_dicts_equal(self) -> bool:
        if len(self.dict1) != len(self.dict2):
            return False
        for key in self.dict1:
            if key not in self.dict2 or self.dict1[key] != self.dict2[key]:
                return False
        return True

if __name__ == '__main__':
    sample_dict1 = {'a': 1, 'b': 2}
    sample_dict2 = {'a': 1, 'b': 2}
    comparator = DictComparator(sample_dict1, sample_dict2)
    result = comparator.are_dicts_equal()
    print(result)