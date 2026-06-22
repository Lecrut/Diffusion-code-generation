class DictFilter:
    @staticmethod
    def filter_negative_values(input_dict):
        return [(key, value) for key, value in input_dict.items() if value >= 0]

if __name__ == '__main__':
    sample_dict = {'a': -1, 'b': 2, 'c': 3, 'd': -4}
    filtered_result = DictFilter.filter_negative_values(sample_dict)
    print(filtered_result)