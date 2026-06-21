def min_of_floats(float_list):
    valid_nums = [num for num in float_list if isinstance(num, (int, float))]
    return min(valid_nums) if valid_nums else None

if __name__ == '__main__':
    sample_values = [3.14, 2.71, 'a', None, 0, -1.5]
    print(min_of_floats(sample_values))