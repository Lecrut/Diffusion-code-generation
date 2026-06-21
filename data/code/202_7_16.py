def find_largest_in_range(start, end):
    if start > end:
        raise ValueError("Start value must be less than or equal to end value")
    
    largest = start
    for i in range(start + 1, end + 1):
        if i > largest:
            largest = i
    
    return largest

if __name__ == '__main__':
    start = 5
    end = 15
    print(f"Range: {start}-{end}, Largest: {find_largest_in_range(start, end)}")
    
    start = -10
    end = 5
    print(f"Range: {start}-{end}, Largest: {find_largest_in_range(start, end)}")
    
    start = 0
    end = 0
    try:
        print(f"Range: {start}-{end}, Largest: {find_largest_in_range(start, end)}")
    except ValueError as e:
        print(e)