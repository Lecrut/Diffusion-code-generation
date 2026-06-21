def min_float_value(mixed_list):
    return min(float(item) for item in mixed_list)

if __name__ == '__main__':
    sample_values = [3, 5.5, '2', -1, 0]
    print(min_float_value(sample_values))