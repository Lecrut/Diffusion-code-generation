def find_maximum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    
    maximum = data[0]
    for item in data[1:]:
        if item > maximum:
            maximum = item
    
    return maximum

if __name__ == '__main__':
    sample_list = [3, 5, 1, 2, 4]
    print(f"Maximum of {sample_list}: {find_maximum(sample_list)}")