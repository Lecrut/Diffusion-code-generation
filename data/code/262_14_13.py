def find_min_max(data):
    if not data:
        return None, None
    elif len(data) == 1:
        return data[0], data[0]
    
    mid = len(data) // 2
    left_min, left_max = find_min_max(data[:mid])
    right_min, right_max = find_min_max(data[mid:])
    
    return min(left_min, right_min), max(left_max, right_max)

if __name__ == '__main__':
    sample_list = [15, 3, 88, 42, 9, 71]
    minimum_val, maximum_val = find_min_max(sample_list)
    print(f"List: {sample_list}")
    print(f"Minimum: {minimum_val}")
    print(f"Maximum: {maximum_val}")