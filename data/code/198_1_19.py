def find_smallest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    
    smallest = data[0]
    for element in data[1:]:
        if element < smallest:
            smallest = element
    
    return smallest

if __name__ == '__main__':
    sample_lists = [
        [5, 2, 8, 1, 9],
        [-10, 0, -5, 3],
        [42],
        [7],
        []
    ]
    
    for lst in sample_lists:
        try:
            print(f"The smallest element in {lst} is: {find_smallest(lst)}")
        except ValueError as e:
            print(e)