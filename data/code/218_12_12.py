class MinValueFinder:
    DEFAULT_VALUE = float('inf')

    @staticmethod
    def find_min_value(input_dict):
        if not input_dict:
            return MinValueFinder.DEFAULT_VALUE

        try:
            values = list(input_dict.values())
            return min(values)
        except TypeError:
            raise ValueError("Dictionary contains non-comparable values.")

if __name__ == '__main__':
    sample_dict = {'a': 3, 'b': 1, 'c': 2}
    result = MinValueFinder.find_min_value(sample_dict)
    print(result)