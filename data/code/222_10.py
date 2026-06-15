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
    list2 = [-10, 5, 0, -20, 100]
    list3 = [7]
    list4 = []
    print(f"Minimum of {list1}: {find_minimum(list1)}")
    print(f"Minimum of {list2}: {find_minimum(list2)}")
    print(f"Minimum of {list3}: {find_minimum(list3)}")
    try:
        print(f"Minimum of {list4}: {find_minimum(list4)}")
    except ValueError as e:
        print(f"Error for {list4}: {e}")