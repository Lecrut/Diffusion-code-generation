def min_of_floats(float_list):
    valid_numbers = [num for num in float_list if isinstance(num, (int, float))]
    return min(valid_numbers) if valid_numbers else None

if __name__ == '__main__':
    test_values = [3.14, 2.718, 'a', 0, -1.618, None]
    minimum_value = min_of_floats(test_values)
    print(minimum_value)