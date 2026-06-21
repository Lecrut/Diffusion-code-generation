def concatenate_lists(list1, list2):
    return list1 + list2

if __name__ == '__main__':
    sample_list_a = [100, 200, 300]
    sample_list_b = [400, 500, 600]
    combined_list = concatenate_lists(sample_list_a, sample_list_b)
    print(combined_list)