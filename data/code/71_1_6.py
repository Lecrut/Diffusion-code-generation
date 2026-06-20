def find_middle_element(lst):
    length = len(lst)
    mid_index = length // 2
    return lst[mid_index]
if __name__ == '__main__':
    print(find_middle_element([1, 2, 3, 4, 5]))
    print(find_middle_element([1, 2, 3, 4]))