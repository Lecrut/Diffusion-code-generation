class DictionaryComparer:
    def __init__(self, dict1, dict2):
        self.dict1 = dict1
        self.dict2 = dict2

    def compare(self):
        sum1 = sum(self.dict1.values())
        sum2 = sum(self.dict2.values())
        if sum1 > sum2:
            return "dict1 is greater"
        elif sum1 < sum2:
            return "dict2 is greater"
        else:
            return "dictionaries are equal"

if __name__ == '__main__':
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict2 = {'x': 4, 'y': 5, 'z': 6}
    comparer = DictionaryComparer(dict1, dict2)
    result = comparer.compare()
    print(result)