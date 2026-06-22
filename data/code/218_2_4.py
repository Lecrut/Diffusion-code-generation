def find_min_value(float_list):
    if not float_list:
        raise ValueError("List is empty")
    min_val = float_list[0]
    for num in float_list:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    sample_values = [3.14, 2.71, 1.618, 0.577, -1.414]
    print(find_min_value(sample_values))