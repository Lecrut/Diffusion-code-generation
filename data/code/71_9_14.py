def find_middle_element(lst):
    n = len(lst)
    middle_index = (n - 1) // 2
    return lst[middle_index]

if __name__ == '__main__':
    sample_list = [7, 3, 5, 9, 1]
    middle_element = find_middle_element(sample_list)
    print(middle_element)