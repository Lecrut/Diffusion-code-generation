class MinFinder:

    def __init__(self, default=None):
        self.default = default

    def find_smallest(self, dictionary):
        if not dictionary or not dictionary.values():
            return self.default
        try:
            return min(dictionary.values())
        except ValueError:
            raise ValueError('Dictionary contains non-comparable values.')
if __name__ == '__main__':
    finder = MinFinder(default=0)
    sample_dict = {'a': 5, 'b': -3, 'c': 8}
    result = finder.find_smallest(sample_dict)
    print(result)