def sum_numeric_values(data):
    return sum(value for value in data.values() if isinstance(value, (int, float)))

if __name__ == '__main__':
    sample_data = {
        'a': 10,
        'b': 20.5,
        'c': 'text',
        'd': 30
    }
    print(sum_numeric_values(sample_data))