MAX_VALUE = float('inf')
MIN_VALUE = float('-inf')

def calculate_value_difference(data):
    max_val = MIN_VALUE
    min_val = MAX_VALUE
    
    for value in data.values():
        if value > max_val:
            max_val = value
        elif value < min_val:
            min_val = value
    
    return max_val - min_val

if __name__ == '__main__':
    sample_data = {
        'a': 10,
        'b': 20,
        'c': 5,
        'd': 30
    }
    print(calculate_value_difference(sample_data))