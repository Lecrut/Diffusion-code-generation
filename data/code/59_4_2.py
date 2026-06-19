def find_middle_element(lst):
    n = len(lst)
    middle_index = n // 2
    return lst[middle_index]

if __name__ == '__main__':
    sample_list = [3.1, 4.5, 6.7, 8.9, 10.2]
    print(find_middle_element(sample_list))