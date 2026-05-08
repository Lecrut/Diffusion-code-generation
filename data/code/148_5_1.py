def find_largest(data):
    if not data:
        raise ValueError("List cannot be empty")
    largest = data[0]
    for element in data[1:]:
        if element > largest:
            largest = element
    return largest
if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6]
    largest_element = find_largest(sample_list)
    print(largest_element)