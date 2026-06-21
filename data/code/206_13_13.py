def min_of_floats(float_list):
    valid_floats = [x for x in float_list if isinstance(x, (int, float))]
    return min(valid_floats) if valid_floats else None

if __name__ == '__main__':
    sample_values = [3.14, 2.71, 'a', 0, -1.5]
    print(min_of_floats(sample_values))