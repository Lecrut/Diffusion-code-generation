def find_middle_element(lst):
    length = len(lst)
    mid_index = length // 2
    if length % 2 == 0:
        return (lst[mid_index - 1], lst[mid_index])
    else:
        return lst[mid_index]
if __name__ == '__main__':
    print(find_middle_element([1, 2, 3, 4, 5]))
    print(find_middle_element([1, 2, 3, 4]))