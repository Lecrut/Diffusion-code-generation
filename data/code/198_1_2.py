def find_smallest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    smallest = data[0]
    for element in data[1:]:
        if element < smallest:
            smallest = element
    return smallest
if __name__ == '__main__':
    list1 = [3, 1, 4, 1, 5, 9, 2]
    print(find_smallest(list1))
    list2 = [-10, 0, 5, -20, 3]
    print(find_smallest(list2))
    list3 = [42]
    print(find_smallest(list3))
    list4 = [100, 50, 25, 75]
    print(find_smallest(list4))