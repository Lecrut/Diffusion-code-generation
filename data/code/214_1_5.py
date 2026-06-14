def find_minimum(data):
    if not data:
        return None
    minimum = data[0]
    for item in data[1:]:
        if item < minimum:
            minimum = item
    return minimum
if __name__ == '__main__':
    list1 = [5, 2, 8, 1, 9]
    list2 = [-10, 0, 5, -3]
    list3 = []
    list4 = [42]
    list5 = [7.5, 3.14, 1.618]
    print(f"Minimum of {list1}: {find_minimum(list1)}")
    print(f"Minimum of {list2}: {find_minimum(list2)}")
    print(f"Minimum of {list3}: {find_minimum(list3)}")
    print(f"Minimum of {list4}: {find_minimum(list4)}")
    print(f"Minimum of {list5}: {find_minimum(list5)}")