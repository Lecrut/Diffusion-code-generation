def find_extremes(values):
    if not values:
        raise ValueError("List cannot be empty")
    
    min_value = float('inf')
    max_value = float('-inf')
    
    for value in values:
        if value < min_value:
            min_value = value
        if value > max_value:
            max_value = value
    
    return min_value, max_value

def calculate_difference(values):
    min_val, max_val = find_extremes(values)
    return max_val - min_val

if __name__ == '__main__':
    sample_values = [15, 3, 20, 9, 7]
    result = calculate_difference(sample_values)
    print(result)