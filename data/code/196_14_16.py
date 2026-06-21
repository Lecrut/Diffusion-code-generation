def concatenate_lists(list1, list2):
    return list1 + list2

if __name__ == '__main__':
    initial_list = [10, 20, 30]
    additional_elements = [40, 50, 60]
    final_result = concatenate_lists(initial_list, additional_elements)
    print(final_result)