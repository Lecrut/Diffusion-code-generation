MINIMUM = float('inf')
MAXIMUM = float('-inf')

def find_min_max(data):
    if not data:
        return None, None
    
    local_min = MINIMUM
    local_max = MAXIMUM
    
    for element in data:
        if element < local_min:
            local_min = element
        elif element > local_max:
            local_max = element
    
    return local_min, local_max

if __name__ == '__main__':
    sample_list = [3.14, 1.618, 2.718, -0.5, 100.0, -50.2]
    minimum_val, maximum_val = find_min_max(sample_list)
    print(f"Minimum: {minimum_val}")
    print(f"Maximum: {maximum_val}")