def concatenate_lists(list1, list2):
    return list1 + list2

if __name__ == '__main__':
    first_list = [7, 8, 9]
    second_list = [10, 11, 12]
    combined_list = concatenate_lists(first_list, second_list)
    print(combined_list)