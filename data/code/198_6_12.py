def find_smallest(data):
    if not data:
        return None
    smallest = data[0]
    for item in data[1:]:
        if item < smallest:
            smallest = item
    return smallest

if __name__ == '__main__':
    sample_data = [7, 2, 9, 5, 3, 8, 1, 6, 4]
    result = find_smallest(sample_data)
    print(result)