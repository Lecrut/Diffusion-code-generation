def find_min_max(values):
    min_value = float('inf')
    max_value = float('-inf')
    for value in values:
        if value < min_value:
            min_value = value
        elif value > max_value:
            max_value = value
    return min_value, max_value

if __name__ == '__main__':
    sample_values = (3, 1, 4, 1, 5, 9, 2, 6, 5, 3)
    min_val, max_val = find_min_max(sample_values)
    print(f"Sample Values: {sample_values}")
    print(f"Minimum Value: {min_val}, Maximum Value: {max_val}")