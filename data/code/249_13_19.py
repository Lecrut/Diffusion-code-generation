MAX_VALUE = float('-inf')

def find_largest_manually(data):
    if not data:
        raise ValueError("The list cannot be empty")
    
    largest = MAX_VALUE
    for element in data:
        if element > largest:
            largest = element
    
    return largest

if __name__ == '__main__':
    sample_list = [15, 8, 42, 3, 99, 27]
    result = find_largest_manually(sample_list)
    print(result)