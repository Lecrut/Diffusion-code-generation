def find_middle_element(lst):
    if len(lst) == 0:
        raise ValueError("The list is empty")
    middle_index = len(lst) // 2
    return lst[middle_index]

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2]
    print(find_middle_element(sample_list))