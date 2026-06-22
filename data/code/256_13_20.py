def find_min_max(data):
    min_val = float('inf')
    max_val = float('-inf')
    for value in data:
        if value < min_val:
            min_val = value
        elif value > max_val:
            max_val = value
    return min_val, max_val

def calculate_range(min_val, max_val):
    return max_val - min_val

if __name__ == '__main__':
    sample_data = [15, 22, 37, 48, 65]
    min_value, max_value = find_min_max(sample_data)
    print(calculate_range(min_value, max_value))