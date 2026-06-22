import math

def find_min_with_nan(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    
    min_value = float('inf')
    for value in data:
        if math.isnan(value):
            continue
        if value < min_value:
            min_value = value
    
    return min_value if min_value != float('inf') else None

if __name__ == '__main__':
    sample_list = [45, 12, float('nan'), 3, 56, 7]
    result = find_min_with_nan(sample_list)
    print(result)