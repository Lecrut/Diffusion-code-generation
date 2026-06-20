def find_middle_element(lst):
    n = len(lst)
    if n == 0:
        raise ValueError('List is empty')
    middle_index = n // 2
    return lst[middle_index]
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    print(find_middle_element(list1))
    list2 = [10, 20, 30, 40, 50, 60]
    print(find_middle_element(list2))
    list3 = [7]
    print(find_middle_element(list3))