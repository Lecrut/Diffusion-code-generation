class MaxValueFinder:
    MAX_DICT = {
        'a': 10,
        'b': 20,
        'c': 5,
        'd': 30
    }

    @staticmethod
    def find_max_value(dictionary):
        return max(dictionary.values()), max(dictionary, key=dictionary.get)

if __name__ == '__main__':
    finder = MaxValueFinder()
    max_val, max_key = finder.find_max_value(MaxValueFinder.MAX_DICT)
    print(f"Key with maximum value: {max_key}")
    print(f"Maximum value: {max_val}")