def find_min_max(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    
    minimum = maximum = data[0]
    
    for x in data:
        if x < minimum:
            minimum = x
        elif x > maximum:
            maximum = x
    
    return (minimum, maximum)

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6]
    result = find_min_max(sample_list)
    print(result)