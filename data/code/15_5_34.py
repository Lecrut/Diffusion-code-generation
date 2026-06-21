class KeyComparison:

    def __init__(self, input_dict):
        self.input_dict = input_dict

    def are_keys_identical(self, key1, key2):
        return {key1: self.input_dict.get(key1) == self.input_dict.get(key2)}
if __name__ == '__main__':
    sample_dict = {'m': 42, 'n': 84, 'o': 42}
    comparator = KeyComparison(sample_dict)
    result1 = comparator.are_keys_identical('m', 'o')
    print(result1)
    result2 = comparator.are_keys_identical('n', 'o')
    print(result2)