class NumberFilter:
    @staticmethod
    def is_valid_number(number):
        return isinstance(number, (int, float)) and number >= 0

    @classmethod
    def filter_valid_numbers(cls, data):
        return [number for number in data if cls.is_valid_number(number)]

def determine_the_largest_number_present_filter_valid(data):
    valid_numbers = NumberFilter.filter_valid_numbers(data)
    if not valid_numbers:
        return None
    largest_number = max(valid_numbers)
    return largest_number

if __name__ == '__main__':
    mock_data = [45, 'a', 89, -3, 67.5, None]
    result = determine_the_largest_number_present_filter_valid(mock_data)
    print(result)