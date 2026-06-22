def get_middle_element(lst):
    if not lst:
        raise ValueError("List is empty")
    return lst[len(lst) // 2]

if __name__ == '__main__':
    odd_list = [1, 2, 3, 4, 5]
    even_list = [1, 2, 3, 4]
    single_element = [42]
    print(get_middle_element(odd_list))
    print(get_middle_element(even_list))
    print(get_middle_element(single_element))