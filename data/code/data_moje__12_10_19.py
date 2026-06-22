def get_middle_element(lst):
    if not lst:
        return None
    return lst[len(lst) // 2]

if __name__ == '__main__':
    empty_list = []
    odd_list = [1, 3, 5, 7, 9]
    even_list = [2, 4, 6, 8]

    result_empty = get_middle_element(empty_list)
    result_odd = get_middle_element(odd_list)
    result_even = get_middle_element(even_list)

    print(result_empty)
    print(result_odd)
    print(result_even)