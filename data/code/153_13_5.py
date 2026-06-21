class DictKeyChecker:

    def __init__(self, list_of_dicts):
        self.list_of_dicts = list_of_dicts

    def key_exists(self, key):
        return any((key in d for d in self.list_of_dicts))
if __name__ == '__main__':
    sample_dicts = [{'a': 1}, {'b': 2}, {'c': 3}]
    checker = DictKeyChecker(sample_dicts)
    print(checker.key_exists('b'))
    print(checker.key_exists('d'))