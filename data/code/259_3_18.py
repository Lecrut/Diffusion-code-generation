def find_min_max(values):
    if not values:
        raise ValueError("The list is empty")
    
    min_value = max_value = values[0]
    
    for value in values[1:]:
        if value < min_value:
            min_value = value
        elif value > max_value:
            max_value = value
    
    return min_value, max_value

if __name__ == '__main__':
    sample_values = [3.141592653589793, 2.718281828459045, 1.618033988749895, 0.5772156649015328]
    min_value, max_value = find_min_max(sample_values)
    print(f"Minimum: {min_value}, Maximum: {max_value}")