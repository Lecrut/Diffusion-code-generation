def find_smallest(data):
    smallest = data[0]
    for item in data[1:]:
        if item < smallest:
            smallest = item
    return smallest
if __name__ == '__main__':
    my_list = [3, 1, 4, 1, 5, 9, 2]
    result = find_smallest(my_list)
    print(result)