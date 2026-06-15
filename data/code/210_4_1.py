def find_range(data):
    if not data:
        return None
    minimum = data[0]
    maximum = data[0]
    for x in data:
        if x < minimum:
            minimum = x
        if x > maximum:
            maximum = x
    return (minimum, maximum)
if __name__ == '__main__':
    list1 = [1, 5, 2, 8, 3]
    list2 = []
    list3 = [10]
    list4 = [-5, -10, 0]
    print(f"Range of {list1}: {find_range(list1)}")
    print(f"Range of {list2}: {find_range(list2)}")
    print(f"Range of {list3}: {find_range(list3)}")
    print(f"Range of {list4}: {find_range(list4)}")