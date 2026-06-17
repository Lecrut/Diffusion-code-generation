def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    minimum = data[0]
    for x in data[1:]:
        if x < minimum:
            minimum = x
    return minimum
if __name__ == '__main__':
    list1 = [3, 1, 4, 1, 5, 9, 2]
    print(find_minimum(list1))
    list2 = [-10, 5, 0, -20, 100]
    print(find_minimum(list2))
    list3 = [42]
    print(find_minimum(list3))
    list4 = [7]
    print(find_minimum(list4))
    list5 = []
    try:
        print(find_minimum(list5))
    except ValueError as e:
        print(e)