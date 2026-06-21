def get_center_element(lst):
    mid = len(lst) // 2
    return lst[mid]

if __name__ == '__main__':
    print(get_center_element([1, 2, 3]))
    print(get_center_element([1, 2, 3, 4, 5]))
    print(get_center_element([10]))
    print(get_center_element([1, 2]))
    print(get_center_element([5, 15, 25, 35, 45, 55, 65]))