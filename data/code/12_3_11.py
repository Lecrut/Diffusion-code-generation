def get_middle_element(lst):
    if not lst:
        return None
    length = len(lst)
    if length % 2 == 1:
        return lst[length // 2]
    else:
        idx = length // 2
        return (lst[idx - 1] + lst[idx]) / 2

if __name__ == '__main__':
    odd_list = [1, 3, 5, 7, 9]
    even_list = [1, 2, 3, 4, 5, 6]
    print(get_middle_element(odd_list))
    print(get_middle_element(even_list))