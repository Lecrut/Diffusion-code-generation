import math

def find_min_with_nan(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    
    min_value = math.inf
    for value in data:
        if not math.isnan(value) and value < min_value:
            min_value = value
    
    return min_value

if __name__ == '__main__':
    sample_list = [45.0, 12.3, float('nan'), 3.14, 56.7, 7.89]
    result = find_min_with_nan(sample_list)
    print(result)