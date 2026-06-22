def find_extremes(data):
    if not data:
        return 0, 0
    max_val = max(data.values())
    min_val = min(data.values())
    return max_val, min_val

def calculate_difference(data):
    max_val, min_val = find_extremes(data)
    return max_val - min_val

if __name__ == '__main__':
    sample_data = {
        'apple': 5,
        'banana': 3,
        'cherry': 8
    }
    print(calculate_difference(sample_data))