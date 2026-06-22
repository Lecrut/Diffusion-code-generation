class KeyComparison:
    def __init__(self, input_dict):
        self.input_dict = input_dict

    def are_keys_identical(self, key1, key2):
        return {key1: self.input_dict.get(key1) == self.input_dict.get(key2)}

if __name__ == '__main__':
    sample_dict = {'x': 5, 'y': 15, 'z': 5}
    comparator = KeyComparison(sample_dict)
    result = comparator.are_keys_identical('x', 'z')
    print(result)