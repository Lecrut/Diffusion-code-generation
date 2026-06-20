def find_middle_element(lst):
    length = len(lst)
    middle_index = length // 2
    return lst[middle_index]

if __name__ == '__main__':
    sample_list = [3, 5, 1, 8, 2]
    print(find_middle_element(sample_list))