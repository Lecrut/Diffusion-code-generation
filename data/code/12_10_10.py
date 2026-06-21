def get_middle_element(lst):
    if not lst:
        return None
    mid_index = len(lst) // 2
    return lst[mid_index]

if __name__ == '__main__':
    print(get_middle_element([1, 2, 3]))
    print(get_middle_element([1, 2, 3, 4]))
    print(get_middle_element([]))
    print(get_middle_element([42]))