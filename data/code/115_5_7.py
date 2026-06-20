def divide_lists(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Lists must be of equal length")
    return [x / y for x, y in zip(list1, list2)]

if __name__ == '__main__':
    a = [10, 20, 30]
    b = [2, 4, 5]
    print(divide_lists(a, b))
    c = [15, 30, 45]
    d = [3, 6, 9]
    print(divide_lists(c, d))
    e = [7, 8, 9]
    f = [0, 1, 2]
    try:
        divide_lists(e, f)
    except ValueError as err:
        print(f"Error caught: {err}")