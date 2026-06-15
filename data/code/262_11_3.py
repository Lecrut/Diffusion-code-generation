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
    list1 = [3, 1, 4, 1, 5, 9, 2, 8]
    list2 = [-10, 5, 0, -50, 100]
    list3 = [7]
    list4 = []
    print(f"List 1: {list1}, Min/Max: {find_min_max(list1)}")
    print(f"List 2: {list2}, Min/Max: {find_min_max(list2)}")
    print(f"List 3: {list3}, Min/Max: {find_min_max(list3)}")
    try:
        find_min_max(list4)
    except ValueError as e:
        print(f"List 4: {list4}, Error: {e}")