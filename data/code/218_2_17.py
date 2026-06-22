def find_min_value(float_list):
    if not float_list:
        return None
    min_val = float_list[0]
    for value in float_list:
        if value < min_val:
            min_val = value
    return min_val

if __name__ == '__main__':
    sample_values = [3.14, 2.71, 1.618, 0.577, -1.414]
    print(find_min_value(sample_values))