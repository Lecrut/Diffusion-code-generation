def calculate_list_sum(data_list):
    if not all(isinstance(item, (int, float)) for item in data_list):
        raise ValueError("All elements in the list must be numbers")
    
    total = 0.0
    for item in data_list:
        total += item
    
    return total

if __name__ == '__main__':
    sample_list = [1.5, 2.5, 3.5]
    result = calculate_list_sum(sample_list)
    print(result)