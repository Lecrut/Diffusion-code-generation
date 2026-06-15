def find_smallest(data):
    if not data:
        return None
    smallest = data[0]
    for element in data[1:]:
        if element < smallest:
            smallest = element
    return smallest
if __name__ == '__main__':
    sample_list = [42, 15, 89, 3, 77, 5]
    smallest_element = find_smallest(sample_list)
    print(smallest_element)