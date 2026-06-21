def concatenate_lists(list1, list2):
    result = list1.copy()
    result.extend(list2)
    return result

if __name__ == '__main__':
    sample_list1 = [i for i in range(1500000)]
    sample_list2 = [i for i in range(1500000, 3000000)]
    concatenated_result = concatenate_lists(sample_list1, sample_list2)
    print(concatenated_result[:5])