MIDDLE_INDEX_CONSTANT = 2

def find_middle_element(lst):
    if not lst:
        raise ValueError('The list is empty')
    middle_index = len(lst) // MIDDLE_INDEX_CONSTANT
    return lst[middle_index]

if __name__ == '__main__':
    sample_odd_list = [7, 14, 21, 28, 35]
    sample_even_list = [9, 18, 27, 36, 45, 54]
    print(find_middle_element(sample_odd_list))
    print(find_middle_element(sample_even_list))