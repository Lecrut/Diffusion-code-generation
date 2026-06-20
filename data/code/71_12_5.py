def find_middle_element(lst):
    length = len(lst)
    if length % 2 == 0:
        return (lst[length // 2 - 1], lst[length // 2])
    else:
        return lst[length // 2]
if __name__ == '__main__':
    print(find_middle_element([1, 2, 3, 4, 5]))
    print(find_middle_element([1, 2, 3, 4]))