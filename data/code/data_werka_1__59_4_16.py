def find_middle_element(lst):
    n = len(lst)
    middle_index = n // 2
    return lst[middle_index]

if __name__ == '__main__':
    sample_list = [3.5, 7.2, 1.8, 4.6, 9.0]
    print(find_middle_element(sample_list))