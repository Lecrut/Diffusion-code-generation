def determine_range(data):
    if not data:
        return None, None
    minimum = maximum = data[0]
    for x in data[1:]:
        if x < minimum:
            minimum = x
        elif x > maximum:
            maximum = x
    return minimum, maximum

if __name__ == '__main__':
    sample_data1 = [7, 3, 9, 2, 5, 1, 8]
    result1 = determine_range(sample_data1)
    print(f"Data: {sample_data1}, Range: {result1}")
    
    sample_data2 = [-1.5, 0.5, -3.5, 2.0, 1.5]
    result2 = determine_range(sample_data2)
    print(f"Data: {sample_data2}, Range: {result2}")