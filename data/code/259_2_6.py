def find_min_max(data_tuple):
    if not data_tuple:
        return None, None
    
    minimum = maximum = data_tuple[0]
    
    for item in data_tuple[1:]:
        if item < minimum:
            minimum = item
        elif item > maximum:
            maximum = item
            
    return minimum, maximum

if __name__ == '__main__':
    sample_data1 = (10, 5, 20, 8, 15)
    min1, max1 = find_min_max(sample_data1)
    print(f"Data: {sample_data1}")
    print(f"Minimum: {min1}, Maximum: {max1}")

    sample_data2 = (-5, 100, 0, -50)
    min2, max2 = find_min_max(sample_data2)
    print(f"Data: {sample_data2}")
    print(f"Minimum: {min2}, Maximum: {max2}")