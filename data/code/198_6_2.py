def find_smallest(data):
    if not data:
        return None
    smallest = data[0]
    for element in data[1:]:
        if element < smallest:
            smallest = element
    return smallest
if __name__ == '__main__':
    sample_list = [5, 12, 3, 8, 1, 15]
    result = find_smallest(sample_list)
    print(result)