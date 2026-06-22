def find_largest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    
    largest = data[0]
    for num in data[1:]:
        if num > largest:
            largest = num
    
    return largest

if __name__ == '__main__':
    sample_list = [15, 8, 22, 3, 45, 10]
    try:
        result = find_largest(sample_list)
        print(result)
    except ValueError as e:
        print(e)