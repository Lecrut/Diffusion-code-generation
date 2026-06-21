class DictionaryComparator:
    @staticmethod
    def sum_of_values(dictionary):
        return sum(dictionary.values())

    @staticmethod
    def compare_dicts(dict1, dict2):
        sum1 = DictionaryComparator.sum_of_values(dict1)
        sum2 = DictionaryComparator.sum_of_values(dict2)
        if sum1 > sum2:
            return "dict1 is greater"
        elif sum1 < sum2:
            return "dict2 is greater"
        else:
            return "dictionaries are equal"

if __name__ == '__main__':
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict2 = {'x': 4, 'y': 5, 'z': 6}
    result = DictionaryComparator.compare_dicts(dict1, dict2)
    print(result)