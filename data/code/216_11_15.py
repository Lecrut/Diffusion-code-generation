def find_middle_element(lst):
    length = len(lst)
    middle_index = length // 2
    return lst[middle_index] if length % 2 != 0 else (lst[middle_index - 1] + lst[middle_index]) / 2

if __name__ == '__main__':
    sample_list = [4, 7, 2, 5, 8]
    print(find_middle_element(sample_list))