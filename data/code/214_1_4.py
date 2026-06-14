def find_minimum(data):
    if not data:
        return None
    minimum = data[0]
    for x in data:
        if x < minimum:
            minimum = x
    return minimum
if __name__ == '__main__':
    list1 = [3, 1, 4, 1, 5, 9, 2]
    list2 = [-10, 5, 0, -3, 8]
    list3 = []
    list4 = [42]
    list5 = [-50, -100, -50]
    print(f"Minimum of {list1}: {find_minimum(list1)}")
    print(f"Minimum of {list2}: {find_minimum(list2)}")
    print(f"Minimum of {list3}: {find_minimum(list3)}")
    print(f"Minimum of {list4}: {find_minimum(list4)}")
    print(f"Minimum of {list5}: {find_minimum(list5)}")