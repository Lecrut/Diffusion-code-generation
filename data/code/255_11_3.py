def find_maximum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    maximum = data[0]
    for x in data[1:]:
        if x > maximum:
            maximum = x
    return maximum
if __name__ == '__main__':
    list1 = [3, 1, 4, 1, 5, 9, 2]
    print(find_maximum(list1))
    list2 = [-10, -5, -20, -1]
    print(find_maximum(list2))
    list3 = [42]
    print(find_maximum(list3))
    list4 = [100]
    print(find_maximum(list4))
    list5 = [7]
    print(find_maximum(list5))