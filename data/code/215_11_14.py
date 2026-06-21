def find_largest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    
    largest = data[0]
    for x in data[1:]:
        if x > largest:
            largest = x
    
    return largest

if __name__ == '__main__':
    sample_lists = [
        [3, 1, 4, 1, 5, 9, 2],
        [-10, -5, -20, -1],
        [42],
        [100, 50, 200, 10]
    ]
    
    for lst in sample_lists:
        print(f"The largest in {lst} is: {find_largest(lst)}")