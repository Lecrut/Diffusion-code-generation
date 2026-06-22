def find_middle_element(lst):
    n = len(lst)
    middle_index = n // 2
    return lst[middle_index]

if __name__ == '__main__':
    sample_list = [1.1, 2.2, 3.3, 4.4, 5.5]
    print(find_middle_element(sample_list))