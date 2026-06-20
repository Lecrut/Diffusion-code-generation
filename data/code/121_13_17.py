class DictSumComparer:
    def __init__(self, dict1, dict2):
        self.dict1 = dict1
        self.dict2 = dict2

    def calculate_sum(self, dictionary):
        return sum(dictionary.values())

    def compare_sums(self):
        sum1 = self.calculate_sum(self.dict1)
        sum2 = self.calculate_sum(self.dict2)
        return self.dict1 if sum1 > sum2 else self.dict2

if __name__ == '__main__':
    comparator = DictSumComparer({'a': 10, 'b': 20}, {'c': 30, 'd': 40})
    result = comparator.compare_sums()
    print(result)