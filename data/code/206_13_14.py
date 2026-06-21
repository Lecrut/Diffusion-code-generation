def min_of_floats(float_list):
    numeric_values = [num for num in float_list if isinstance(num, (int, float))]
    return min(numeric_values) if numeric_values else None

if __name__ == '__main__':
    sample_data = [3.14, 2.718, 'hello', 0.577, None]
    result = min_of_floats(sample_data)
    print(result)