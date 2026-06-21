def concatenate_lists(list_one, list_two):
    combined_list = list_one + list_two
    return combined_list

if __name__ == '__main__':
    sample_list1 = [10, 20, 30]
    sample_list2 = [30, 40, 50]
    result = concatenate_lists(sample_list1, sample_list2)
    print(result)

    sample_list3 = ['red', 'green']
    sample_list4 = ['blue', 'yellow']
    result2 = concatenate_lists(sample_list3, sample_list4)
    print(result2)