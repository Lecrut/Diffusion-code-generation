def find_largest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    largest = data[0]
    for x in data[1:]:
        if x > largest:
            largest = x
    return largest
if __name__ == '__main__':
    list1 = [3, 1, 4, 1, 5, 9, 2]
    print(find_largest(list1))
    list2 = [-10, -5, -20, -1]
    print(find_largest(list2))
    list3 = [7]
    print(find_largest(list3))
    list4 = [42]
    print(find_largest(list4))
    list5 = []
    try:
        print(find_largest(list5))
    except ValueError as e:
        print(e)