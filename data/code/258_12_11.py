import numpy as np

def validate_data(data):
    if not data:
        return False
    for pair in data:
        if not isinstance(pair, (list, tuple)) or len(pair) != 2:
            return False
        try:
            float(pair[0]) + float(pair[1])
        except ValueError:
            return False
    return True

def calculate_average(data):
    if not validate_data(data):
        raise ValueError("Invalid data format")
    total_sum = np.sum([x + y for x, y in data])
    count = len(data) * 2
    return total_sum / count

if __name__ == '__main__':
    sample_data = [(1, 2), (3, 4), (5, 6)]
    print(calculate_average(sample_data))