def find_min_value(float_list):
    if not float_list:
        return None
    min_val = float_list[0]
    for num in float_list[1:]:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    sample_values = [3.5, 2.1, 4.8, 1.9, 2.9]
    print(find_min_value(sample_values))