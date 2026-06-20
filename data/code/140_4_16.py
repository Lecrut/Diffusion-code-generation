class StringFilter:
    INVALID_VALUES = {None, ''}

    @staticmethod
    def is_valid(value):
        return value not in StringFilter.INVALID_VALUES

    @staticmethod
    def filter_entries(input_list):
        return [entry for entry in input_list if StringFilter.is_valid(entry)]

if __name__ == '__main__':
    sample_values = ['hello', '', None, 'world', ' ', 'test']
    filtered_values = StringFilter.filter_entries(sample_values)
    print(filtered_values)