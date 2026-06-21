def calculate_range(data):
    if not data:
        raise ValueError("Data list cannot be empty")
    
    minimum = maximum = data[0]
    
    for x in data[1:]:
        if x < minimum:
            minimum = x
        elif x > maximum:
            maximum = x
    
    return maximum - minimum

if __name__ == '__main__':
    sample_list = [10.5, 2.3, 7.8, 9.4, 3.6]
    print(calculate_range(sample_list))