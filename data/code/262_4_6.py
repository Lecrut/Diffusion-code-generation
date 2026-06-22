def find_min_max(dictionary):
    if not dictionary:
        return None, None
    
    min_val = max_val = next(iter(dictionary.values()))
    
    for value in dictionary.values():
        if value < min_val:
            min_val = value
        elif value > max_val:
            max_val = value
    
    return min_val, max_val

if __name__ == '__main__':
    sample_dict = {'apple': 100, 'banana': 200, 'cherry': 50, 'date': 75}
    result_min, result_max = find_min_max(sample_dict)
    print(f"Minimum value: {result_min}, Maximum value: {result_max}")