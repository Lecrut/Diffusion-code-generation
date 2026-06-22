import math

def find_min_filtered(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    
    filtered_data = [x for x in data if not math.isnan(x)]
    if not filtered_data:
        raise ValueError("All elements are NaN")
    
    minimum = min(filtered_data)
    return minimum

if __name__ == '__main__':
    sample_list = [45.0, 12.3, math.nan, 89.1, 3.0, 56.7, math.nan]
    result = find_min_filtered(sample_list)
    print(result)