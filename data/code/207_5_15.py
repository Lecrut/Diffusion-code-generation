def find_largest_number_in_strings(string_numbers):
    if not string_numbers:
        return None
    try:
        numbers = [int(num) for num in string_numbers]
    except ValueError:
        raise ValueError('All elements must be convertible to integers.')
    max_value = max(numbers)
    return max_value
if __name__ == '__main__':
    sample_data1 = ['34', '78', '12', '90']
    print(find_largest_number_in_strings(sample_data1))
    sample_data2 = ['-5', '-2', '-10', '-1']
    print(find_largest_number_in_strings(sample_data2))
    sample_data3 = ['42']
    print(find_largest_number_in_strings(sample_data3))
    sample_data4 = []
    print(find_largest_number_in_strings(sample_data4))