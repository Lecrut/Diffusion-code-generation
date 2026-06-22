def find_middle_item(lst):
    if not lst:
        raise ValueError('The list is empty')
    n = len(lst)
    middle_index = n // 2
    if n % 2 == 0:
        return (lst[middle_index - 1] + lst[middle_index]) / 2
    else:
        return lst[middle_index]
if __name__ == '__main__':
    sample_list_odd = [1, 3, 5, 7, 9]
    sample_list_even = [1, 2, 3, 4, 5, 6]
    print(find_middle_item(sample_list_odd))
    print(find_middle_item(sample_list_even))