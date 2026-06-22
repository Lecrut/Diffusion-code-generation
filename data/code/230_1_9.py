class DictFilter:
    MIN_VALUE = 0

    @staticmethod
    def filter_dict(input_dict):
        return [(key, value) for key, value in input_dict.items() if value >= DictFilter.MIN_VALUE]

if __name__ == '__main__':
    sample_dict = {'a': -1, 'b': 2, 'c': 3, 'd': -4}
    filtered_result = DictFilter.filter_dict(sample_dict)
    print(filtered_result)