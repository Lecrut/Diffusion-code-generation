def find_minimum(values):
    if not values:
        raise ValueError("List must not be empty")
    
    lowest = values[0]
    for num in values[1:]:
        if num < lowest:
            lowest = num
    return lowest

if __name__ == '__main__':
    sample_values = [3.14, 1.41, 2.72, 0.58, 9.99]
    result = find_minimum(sample_values)
    print(result)