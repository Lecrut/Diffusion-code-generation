def calculate_value_difference(data):
    if not data:
        return 0
    values = list(data.values())
    return max(values) - min(values)

if __name__ == '__main__':
    sample_data = {
        'a': 10,
        'b': 20,
        'c': 5,
        'd': 30
    }
    print(calculate_value_difference(sample_data))