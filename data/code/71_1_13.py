def find_middle_element(lst):
    length = len(lst)
    middle_index = length // 2
    return lst[middle_index]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(find_middle_element(sample_list))