def reverse_list(lst):
    if not isinstance(lst, list):
        raise ValueError("Input must be a list")
    return lst[::-1]

if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7]
    print(reverse_list(data))
    data2 = [10, 20, 30, 40, 50]
    print(reverse_list(data2))
    data3 = [1, 2, 1, 3, 5, 4]
    print(reverse_list(data3))