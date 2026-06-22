def get_middle_element(lst):
    if not lst:
        raise ValueError("List must not be empty")
    length = len(lst)
    if length % 2 == 1:
        return lst[length // 2]
    return lst[length // 2 - 1]

if __name__ == '__main__':
    print(get_middle_element([1, 2, 3, 4, 5]))
    print(get_middle_element([1, 2, 3, 4]))
    print(get_middle_element([10]))
    print(get_middle_element([10, 20]))
    print(get_middle_element([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(get_middle_element([1, 2, 3, 4, 5, 6, 7, 8]))