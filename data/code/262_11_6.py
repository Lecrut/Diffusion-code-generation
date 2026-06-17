def find_min_max(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    minimum = data[0]
    maximum = data[0]
    for x in data:
        if x < minimum:
            minimum = x
        if x > maximum:
            maximum = x
    return (minimum, maximum)
if __name__ == '__main__':
    list1 = [3, 1, 4, 1, 5, 9, 2]
    print(find_min_max(list1))
    list2 = [-10, 0, 55, -3, 100]
    print(find_min_max(list2))
    list3 = [7]
    print(find_min_max(list3))
    list4 = []
    try:
        print(find_min_max(list4))
    except ValueError as e:
        print(e)