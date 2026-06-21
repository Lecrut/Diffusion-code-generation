def get_largest_number(numbers):
    if not numbers:
        return None
    largest = max(numbers)
    return largest

if __name__ == '__main__':
    sample_data = [-10, -5, 22, -8, 3]
    result = get_largest_number(sample_data)
    print(result)

    sample_data_floats = [10.5, 5.1, 22.3, 8.4, 3.9]
    result_floats = get_largest_number(sample_data_floats)
    print(result_floats)