def min_of_floats(float_list):
    valid_numbers = [num for num in float_list if isinstance(num, (int, float))]
    return min(valid_numbers) if valid_numbers else None

if __name__ == '__main__':
    sample_values = [3.14, 2.718, 'a', None, 0, -1]
    result = min_of_floats(sample_values)
    print(result)