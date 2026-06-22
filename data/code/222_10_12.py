def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return min(data)

if __name__ == '__main__':
    list1 = [3, 1, 4, 1, 5, 9, 2]
    list2 = [-10, 0, 5, -2, 8]
    list3 = [42]
    list4 = []
    try:
        print(f"Minimum of {list1}: {find_minimum(list1)}")
        print(f"Minimum of {list2}: {find_minimum(list2)}")
        print(f"Minimum of {list3}: {find_minimum(list3)}")
        print(f"Minimum of {list4}: {find_minimum(list4)}")
    except ValueError as e:
        print(e)