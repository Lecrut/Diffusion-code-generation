def find_smallest(data):
    if not data:
        raise ValueError('Input list cannot be empty')
    smallest = data[0]
    for item in data[1:]:
        if item < smallest:
            smallest = item
    return smallest
if __name__ == '__main__':
    sample_data = [7, 3, 5, 2, 9, 1]
    result = find_smallest(sample_data)
    print(result)