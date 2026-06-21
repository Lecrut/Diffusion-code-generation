def combine_lists(list_alpha, list_beta):
    if not isinstance(list_alpha, list) or not isinstance(list_beta, list):
        raise ValueError("Both arguments must be lists.")
    result = list_alpha.copy()
    result.extend(list_beta)
    return result

if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = [4, 5, 6]
    combined_list = combine_lists(sample_list1, sample_list2)
    print(combined_list)