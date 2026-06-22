class DictMinMax:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def find_min_max(self):
        if not self.dictionary:
            return None, None
        min_val = max_val = next(iter(self.dictionary.values()))
        for value in self.dictionary.values():
            if value < min_val:
                min_val = value
            elif value > max_val:
                max_val = value
        return min_val, max_val

if __name__ == '__main__':
    sample_dict = {'a': 10, 'b': 20, 'c': 5, 'd': 30}
    dict_min_max = DictMinMax(sample_dict)
    min_value, max_value = dict_min_max.find_min_max()
    print(f"Minimum value: {min_value}, Maximum value: {max_value}")