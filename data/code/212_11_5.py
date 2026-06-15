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
    list1 = [1, 5, 2, 8, 3]
    print(calculate_range(list1))
    list2 = [10, 4, 1, 9, 2]
    print(calculate_range(list2))
    list3 = [5]
    print(calculate_range(list3))
    list4 = []
    print(calculate_range(list4))