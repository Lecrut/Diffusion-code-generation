def sum_numeric_values(data):
    return sum(value for value in data.values() if isinstance(value, (int, float)))

if __name__ == '__main__':
    sample_data = {'x': 5, 'y': 3.14, 'z': 'world', 'w': 2}
    result = sum_numeric_values(sample_data)
    print(result)