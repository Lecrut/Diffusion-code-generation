def calculate_range(data):
    if not data:
        return 0
    minimum = data[0]
    maximum = data[0]
    for x in data:
        if x < minimum:
            minimum = x
        if x > maximum:
            maximum = x
    return maximum - minimum
if __name__ == '__main__':
    list1 = [5, 2, 9, 1, 7]
    print(calculate_range(list1))
    list2 = [-10, 5, 0, -3, 8]
    print(calculate_range(list2))
    list3 = [42]
    print(calculate_range(list3))
    list4 = []
    print(calculate_range(list4))