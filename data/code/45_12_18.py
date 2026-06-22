def find_minimum(values):
    if not values:
        raise ValueError("List is empty")
    
    min_val = values[0]
    for num in values[1:]:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    sample_values = [3.14, 1.59, 2.65, 3.58, 9.79, 3.23, 8.46, 2.64, 3.38, 3.27]
    result = find_minimum(sample_values)
    print(result)