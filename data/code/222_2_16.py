import math

def find_min_with_nan(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    
    min_value = float('inf')
    for item in data:
        if math.isnan(item):
            continue
        if item < min_value:
            min_value = item
    
    return min_value if min_value != float('inf') else None

if __name__ == '__main__':
    sample_list = [45.0, 12.3, 89.4, math.nan, 3.0, 56.7, 7.8]
    result = find_min_with_nan(sample_list)
    print(result)