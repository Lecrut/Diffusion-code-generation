class FilterDict:
    MIN_VALUE = 0

    @staticmethod
    def filter(input_dict):
        return [(key, value) for key, value in input_dict.items() if value >= FilterDict.MIN_VALUE]

if __name__ == '__main__':
    sample_dict = {'a': -1, 'b': 2, 'c': 3, 'd': -4}
    filtered_result = FilterDict.filter(sample_dict)
    print(filtered_result)