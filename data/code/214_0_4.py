def find_smallest(data):
    if not data:
        raise ValueError("List cannot be empty")
    smallest = data[0]
    for item in data[1:]:
        if item < smallest:
            smallest = item
    return smallest
if __name__ == '__main__':
    sample_list = [42, 15, 89, 3, 77, 5]
    smallest_value = find_smallest(sample_list)
    print(smallest_value)