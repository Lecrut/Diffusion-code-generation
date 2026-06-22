def find_smallest_element(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    smallest = data[0]
    for item in data[1:]:
        if item < smallest:
            smallest = item
    return smallest

if __name__ == '__main__':
    sample_list = [34, 7, 23, 32, 5, 62]
    print(f"Smallest element: {find_smallest_element(sample_list)}")