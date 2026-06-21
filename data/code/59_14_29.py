def find_middle_item(lst):
    if not lst:
        raise ValueError('The list is empty')
    n = len(lst)
    middle_index = n // 2
    return (lst[middle_index - 1] + lst[middle_index]) / 2 if n % 2 == 0 else lst[middle_index]

if __name__ == '__main__':
    odd_list = [1, 3, 5, 7, 9]
    even_list = [2, 4, 6, 8, 10, 12]
    print(find_middle_item(odd_list))
    print(find_middle_item(even_list))