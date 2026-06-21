def find_smallest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    smallest = data[0]
    for element in data[1:]:
        if element < smallest:
            smallest = element
    return smallest

if __name__ == '__main__':
    sample_list = [2.5, 3.7, 1.4, 6.2, 0.9]
    print(f"The smallest element in {sample_list} is: {find_smallest(sample_list)}")