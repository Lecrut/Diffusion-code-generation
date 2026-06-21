class ItemCountComparer:
    def __init__(self, dict1=None, dict2=None):
        if dict1 is None:
            dict1 = {}
        if dict2 is None:
            dict2 = {}
        self.dict1 = dict1
        self.dict2 = dict2

    def compare(self):
        result = {}
        for key in set(self.dict1) | set(self.dict2):
            count1 = self.dict1.get(key, 0)
            count2 = self.dict2.get(key, 0)
            result[key] = count1 - count2
        return result

if __name__ == '__main__':
    comparer = ItemCountComparer({'apple': 3, 'banana': 5, 'cherry': 2}, {'banana': 2, 'cherry': 4, 'date': 7})
    print(comparer.compare())