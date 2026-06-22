MIN_VALUE = float('inf')
MAX_VALUE = float('-inf')

def calculate_range(data):
    min_val = MIN_VALUE
    max_val = MAX_VALUE
    for value in data:
        if value < min_val:
            min_val = value
        elif value > max_val:
            max_val = value
    return max_val - min_val

if __name__ == '__main__':
    sample_data = [10, 25, 35, 45, 60]
    print(calculate_range(sample_data))