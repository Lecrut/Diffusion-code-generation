def sum_numeric_values(data):
    total = 0
    for value in data.values():
        if isinstance(value, (int, float)):
            total += value
    return total

if __name__ == '__main__':
    sample_dict = {'a': 15, 'b': 25.5, 'c': 'world', 'd': 35}
    result = sum_numeric_values(sample_dict)
    print(result)