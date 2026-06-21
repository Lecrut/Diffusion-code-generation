def min_of_floats(float_list):
    valid_nums = [num for num in float_list if isinstance(num, (int, float))]
    return min(valid_nums) if valid_nums else None

if __name__ == '__main__':
    sample_values = [3.5, 2.1, 'a', 4.8, None, 0.9]
    print(min_of_floats(sample_values))