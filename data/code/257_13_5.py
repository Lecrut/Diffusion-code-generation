def calculate_value_difference(data):
    if not data:
        return 0
    max_value = max(data.values())
    min_value = min(data.values())
    return max_value - min_value

if __name__ == '__main__':
    sample_data = {
        'a': 10,
        'b': 20,
        'c': 5,
        'd': 30
    }
    print(calculate_value_difference(sample_data))