def calculate_value_difference(data):
    if not data:
        return 0
    return max(data.values()) - min(data.values())

if __name__ == '__main__':
    sample_data = {
        'one': 10,
        'two': 20,
        'three': 30,
        'four': 40,
        'five': 50
    }
    print(calculate_value_difference(sample_data))