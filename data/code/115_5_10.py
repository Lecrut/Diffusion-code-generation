def divide_lists(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Lists must be of equal length")
    return [x / y for x, y in zip(list1, list2)]

if __name__ == '__main__':
    A = [10, 20, 30]
    B = [2, 4, 5]
    print(divide_lists(A, B))