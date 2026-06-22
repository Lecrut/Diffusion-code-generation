def find_largest_data_point(numbers):
    validated_input = list(numbers)
    if not validated_input:
        raise ValueError("Input list must not be empty")
    sorted_values = sorted(validated_input, reverse=True)
    largest = sorted_values[0]
    return largest

if __name__ == '__main__':
    test_list = [42, 17, 89, -5, 3.14, 100, 55]
    max_value = find_largest_data_point(test_list)
    print(max_value)