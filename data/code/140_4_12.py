class FilterEmpty:
    EMPTY_VALUES = (None, '')

    @staticmethod
    def filter_valid_entries(input_list):
        return [entry for entry in input_list if entry not in FilterEmpty.EMPTY_VALUES]

if __name__ == '__main__':
    sample_values = ['hello', '', None, 'world', ' ', 'test']
    filtered_values = FilterEmpty.filter_valid_entries(sample_values)
    print(filtered_values)