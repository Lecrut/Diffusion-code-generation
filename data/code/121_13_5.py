class DictSumComparator:
    def __init__(self, dict1, dict2):
        self.dict1 = dict1
        self.dict2 = dict2

    def compare(self):
        sum1 = sum(self.dict1.values())
        sum2 = sum(self.dict2.values())
        return self.dict1 if sum1 > sum2 else self.dict2

if __name__ == '__main__':
    comparator = DictSumComparator({'a': 10, 'b': 20}, {'c': 30, 'd': 40})
    result = comparator.compare()
    print(result)