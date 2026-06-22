class DictRepeater:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def repeat_keys(self, count):
        result = []
        for _ in range(count):
            result.extend(self.dictionary.keys())
        return result

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    repeater = DictRepeater(sample_dict)
    repeated_keys = repeater.repeat_keys(5)
    print(repeated_keys)