def append_lists(list1, list2):
    return list1 + list2

if __name__ == '__main__':
    primary_list = [3, 4, 5]
    supplementary_list = [6, 7, 8]
    concatenated_result = append_lists(primary_list, supplementary_list)
    print(concatenated_result)