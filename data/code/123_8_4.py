def sum_numeric_values(input_dict):
    total = 0
    for value in input_dict.values():
        if isinstance(value, (int, float)):
            total += value
    return total

if __name__ == '__main__':
    sample_dict = {'x': 50, 'y': 75.25, 'z': 'world', 'w': 30}
    result = sum_numeric_values(sample_dict)
    print(result)