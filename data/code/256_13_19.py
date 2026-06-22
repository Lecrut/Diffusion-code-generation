MIN_VAL = float('inf')
MAX_VAL = float('-inf')

def calculate_range(data):
    min_val = MIN_VAL
    max_val = MAX_VAL
    for value in data:
        if value < min_val:
            min_val = value
        elif value > max_val:
            max_val = value
    return max_val - min_val

if __name__ == '__main__':
    sample_data = [10, 25, 35, 45, 60]
    print(calculate_range(sample_data))