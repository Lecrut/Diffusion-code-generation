def find_middle_element(lst):
    length = len(lst)
    middle_index = length // 2
    return lst[middle_index]

if __name__ == '__main__':
    sample_list = [7.1, 8.2, 9.3, 10.4]
    print(find_middle_element(sample_list))