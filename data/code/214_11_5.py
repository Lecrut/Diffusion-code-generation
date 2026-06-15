def find_minimum(data):
    if not data:
        raise ValueError("Input iterable cannot be empty")
    minimum = data[0]
    for item in data[1:]:
        if item < minimum:
            minimum = item
    return minimum
if __name__ == '__main__':
    list1 = [5, 2, 8, 1, 9, 3]
    list2 = [-10, 50, 0, -5, 100]
    list3 = [42]
    list4 = [7]
    empty_list = []
    print(f"Minimum of {list1}: {find_minimum(list1)}")
    print(f"Minimum of {list2}: {find_minimum(list2)}")
    print(f"Minimum of {list3}: {find_minimum(list3)}")
    print(f"Minimum of {list4}: {find_minimum(list4)}")
    try:
        find_minimum(empty_list)
    except ValueError as e:
        print(f"Error for empty list: {e}")