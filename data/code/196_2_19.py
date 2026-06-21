def concatenate_lists(list1, list2):
    return list1 + list2

if __name__ == '__main__':
    first_list = [10, 20, 30]
    second_list = [40, 50, 60]
    combined_list = concatenate_lists(first_list, second_list)
    print(combined_list)