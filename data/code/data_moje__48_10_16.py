def linear_search_max(data):
    if not data:
        return None
    
    max_val = data[0]
    for value in data:
        if value > max_val:
            max_val = value
            
    return max_val

if __name__ == '__main__':
    sample_values = [10, 5, 8, 20, 3, 15, 7]
    result = linear_search_max(sample_values)
    print(result)