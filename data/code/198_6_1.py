def find_smallest(data):
    if not data:
        return None
    smallest = data[0]
    for element in data[1:]:
        if element < smallest:
            smallest = element
    return smallest
if __name__ == '__main__':
    my_list = [3, 1, 4, 1, 5, 9, 2, 6]
    result = find_smallest(my_list)
    print(result)