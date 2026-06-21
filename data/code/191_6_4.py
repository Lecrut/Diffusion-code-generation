def combine_lists(list_alpha, list_beta):
    result = []
    for item in list_alpha:
        result.append(item)
    for item in list_beta:
        result.append(item)
    return result

if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = [4, 5, 6]
    combined_list = combine_lists(sample_list1, sample_list2)
    print(combined_list)