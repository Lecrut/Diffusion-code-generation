def find_lowest(values):
    if not values:
        return None
    
    lowest = values[0]
    
    for num in values[1:]:
        if num < lowest:
            lowest = num
            
    return lowest

if __name__ == '__main__':
    sample_data = [3.14, 1.59, 2.65, 3.58, 9.79, 3.23, 8.46, 2.64]
    
    result = find_lowest(sample_data)
    
    print(result)