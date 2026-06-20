def find_middle_element(lst):
    length = len(lst)
    middle_index = length // 2
    return lst[middle_index]

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(find_middle_element(sample_list))