class DictComparator:

    def __init__(self):
        self.only_in_dict1 = {}
        self.only_in_dict2 = {}
        self.diff_values = {}

    @staticmethod
    def compare(dict1, dict2):
        comparator = DictComparator()
        for key in set(dict1) | set(dict2):
            if key not in dict1:
                comparator.only_in_dict2[key] = dict2[key]
            elif key not in dict2:
                comparator.only_in_dict1[key] = dict1[key]
            elif dict1[key] != dict2[key]:
                comparator.diff_values[key] = (dict1[key], dict2[key])
        return comparator
if __name__ == '__main__':
    sample_dict1 = {'a': 1, 'b': 2, 'c': 3}
    sample_dict2 = {'b': 2, 'c': 4, 'd': 5}
    comparator = DictComparator.compare(sample_dict1, sample_dict2)
    print(comparator.only_in_dict1)
    print(comparator.only_in_dict2)
    print(comparator.diff_values)