def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    minimum = data[0]
    for item in data[1:]:
        if item < minimum:
            minimum = item
    return minimum

if __name__ == '__main__':
    list1 = [5, 2, 8, 1, 9]
    list2 = [-10, 0, -3]
    empty_list = []
    try:
        print(f"Minimum of {list1}: {find_minimum(list1)}")
        print(f"Minimum of {list2}: {find_minimum(list2)}")
        find_minimum(empty_list)
    except ValueError as e:
        print(e)