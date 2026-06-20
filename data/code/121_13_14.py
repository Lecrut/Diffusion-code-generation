class DictSumComparator:
    def __init__(self, dict1, dict2):
        self.dict1 = dict1
        self.dict2 = dict2
    
    def get_sum(self, dictionary):
        return sum(dictionary.values())
    
    def compare(self):
        sum1 = self.get_sum(self.dict1)
        sum2 = self.get_sum(self.dict2)
        if sum1 > sum2:
            return self.dict1
        else:
            return self.dict2

if __name__ == '__main__':
    comparator = DictSumComparator({'a': 10, 'b': 20}, {'c': 30, 'd': 40})
    result = comparator.compare()
    print(result)