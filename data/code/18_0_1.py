def get_middle_element(lst):
    length = len(lst)
    if length == 0:
        return None
    index = length // 2
    return lst[index]

if __name__ == '__main__':
    odd_list = [10, 20, 30, 40, 50]
    even_list = [1, 2, 3, 4, 5, 6]
    middle_odd = get_middle_element(odd_list)
    middle_even = get_middle_element(even_list)
    print(middle_odd)
    print(middle_even)