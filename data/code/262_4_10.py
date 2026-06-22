class MinMaxFinder:
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
    sample_dict = {'apple': 50, 'banana': 30, 'cherry': 20, 'date': 80}
    finder = MinMaxFinder(sample_dict)
    min_value, max_value = finder.find_min_max()
    print(f"Minimum value: {min_value}, Maximum value: {max_value}")