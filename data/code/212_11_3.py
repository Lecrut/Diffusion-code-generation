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
    list2 = [-10, 0, 5, -5, 10]
    list3 = [7]
    list4 = []
    print(calculate_range(list1))
    print(calculate_range(list2))
    print(calculate_range(list3))
    print(calculate_range(list4))