def get_middle_element(lst):
    length = len(lst)
    if length == 0:
        return None
    mid_index = length // 2
    return lst[mid_index]

if __name__ == '__main__':
    odd_list = [1, 2, 3, 4, 5]
    even_list = [10, 20, 30, 40]
    odd_mid = get_middle_element(odd_list)
    even_mid = get_middle_element(even_list)
    print(odd_mid)
    print(even_mid)