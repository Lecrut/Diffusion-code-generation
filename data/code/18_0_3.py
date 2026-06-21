def find_middle_element(lst):
    if not lst:
        raise ValueError("List is empty")
    mid_index = len(lst) // 2
    if len(lst) % 2 == 0:
        return (lst[mid_index - 1], lst[mid_index])
    else:
        return lst[mid_index]

if __name__ == '__main__':
    odd_list = [1, 2, 3, 4, 5]
    even_list = [1, 2, 3, 4, 5, 6]
    print(find_middle_element(odd_list))
    print(find_middle_element(even_list))