def get_middle_element(lst):
    if not lst:
        return None
    length = len(lst)
    if length % 2 == 0:
        return lst[length // 2]
    return lst[length // 2]

if __name__ == '__main__':
    print(get_middle_element([1, 2, 3, 4, 5]))
    print(get_middle_element([1, 2, 3, 4]))
    print(get_middle_element([]))