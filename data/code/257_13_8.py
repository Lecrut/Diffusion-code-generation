def calculate_value_difference(data):
    if not data:
        return 0
    return max(data.values()) - min(data.values())

if __name__ == '__main__':
    sample_data = {'a': 10, 'b': 20, 'c': 5}
    print(calculate_value_difference(sample_data))