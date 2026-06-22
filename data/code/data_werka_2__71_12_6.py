def get_middle_element(lst):
    if not lst:
        raise ValueError("List must not be empty")
    n = len(lst)
    if n % 2 == 1:
        return lst[n // 2]
    mid1 = lst[n // 2 - 1]
    mid2 = lst[n // 2]
    return (mid1 + mid2) / 2

if __name__ == '__main__':
    odd_list = [1, 2, 3, 4, 5]
    even_list = [1, 2, 3, 4]
    print(get_middle_element(odd_list))
    print(get_middle_element(even_list))