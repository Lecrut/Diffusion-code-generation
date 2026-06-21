def find_middle_element(lst):
    if not lst:
        raise ValueError('The list is empty')
    index = len(lst) // 2
    return lst[index]
if __name__ == '__main__':
    sample_list_odd = [10, 20, 30, 40, 50]
    sample_list_even = [10, 20, 30, 40, 50, 60]
    print(find_middle_element(sample_list_odd))
    print(find_middle_element(sample_list_even))