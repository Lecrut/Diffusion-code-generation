def find_middle_element(lst):
    if not lst:
        return None
    middle_index = len(lst) // 2
    if len(lst) % 2 == 0:
        return (lst[middle_index - 1], lst[middle_index])
    else:
        return lst[middle_index]

if __name__ == '__main__':
    odd_list = [1, 2, 3, 4, 5]
    even_list = [1, 2, 3, 4, 5, 6]
    print(find_middle_element(odd_list))
    print(find_middle_element(even_list))