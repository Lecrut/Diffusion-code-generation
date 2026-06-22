def find_smallest_element(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    smallest = data[0]
    for item in data[1:]:
        if item < smallest:
            smallest = item
    return smallest

if __name__ == '__main__':
    sample_list = [3, 7, 2, 5, 1]
    print(f"The smallest element is: {find_smallest_element(sample_list)}")