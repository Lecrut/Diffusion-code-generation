def get_middle(lst):
    if not lst:
        return None
    length = len(lst)
    if length % 2 == 1:
        return lst[length // 2]
    else:
        mid = length // 2
        return lst[mid]

if __name__ == '__main__':
    odd_list = [1, 2, 3, 4, 5]
    even_list = [1, 2, 3, 4]
    empty_list = []

    result_odd = get_middle(odd_list)
    result_even = get_middle(even_list)
    result_empty = get_middle(empty_list)

    print(result_odd)
    print(result_even)
    print(result_empty)