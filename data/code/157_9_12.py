def find_smallest_iterative(data):
    if not data:
        raise ValueError('Input list cannot be empty')
    smallest = data[0]
    for element in data[1:]:
        if element < smallest:
            smallest = element
    return smallest
if __name__ == '__main__':
    sample_list = [45, 23, 89, 67, 10, 33, 78]
    try:
        result = find_smallest_iterative(sample_list)
        print(result)
    except ValueError as e:
        print(f'Error: {e}')