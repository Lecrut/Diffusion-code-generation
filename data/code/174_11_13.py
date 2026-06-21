class DictMerger:

    def __init__(self):
        self.result = {}

    def merge(self, dict1, dict2):
        for key in set(dict1) | set(dict2):
            value1 = dict1.get(key, 0)
            value2 = dict2.get(key, 0)
            self.result[key] = value1 + value2
if __name__ == '__main__':
    merger = DictMerger()
    sample_dict1 = {'a': 1, 'b': 2, 'c': 3}
    sample_dict2 = {'b': 3, 'c': 4, 'd': 5}
    merger.merge(sample_dict1, sample_dict2)
    print(merger.result)