def find_min_max(iterable):
    if not iterable:
        return None, None
    
    current_min = current_max = next(iter(iterable))
    
    for item in iterable:
        if item < current_min:
            current_min = item
        elif item > current_max:
            current_max = item
    
    return current_min, current_max

if __name__ == '__main__':
    data1 = [7, 3, 9, 2, 5]
    print("Data 1:")
    min_val, max_val = find_min_max(data1)
    print(f"Min: {min_val}, Max: {max_val}")