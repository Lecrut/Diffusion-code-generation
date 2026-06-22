def find_largest_manual(data):
    if not data:
        raise ValueError("The list is empty")
    
    largest = data[0]
    for element in data[1:]:
        if element > largest:
            largest = element
    
    return largest

if __name__ == '__main__':
    sample_list = [15, 8, 42, 3, 99, 27]
    result = find_largest_manual(sample_list)
    print(result)