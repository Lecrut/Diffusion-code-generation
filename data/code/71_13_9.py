def find_middle_element(lst):
    return lst[len(lst) // 2 - 1] if len(lst) % 2 == 0 else lst[len(lst) // 2]
if __name__ == '__main__':
    print(find_middle_element([1, 2, 3, 4, 5]))
    print(find_middle_element([1, 2, 3, 4]))