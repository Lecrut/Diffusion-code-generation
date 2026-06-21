def concatenate_lists(list1, list2):
    result = list1.copy()
    result.extend(list2)
    return result

if __name__ == '__main__':
    sample_list1 = [i for i in range(5000)]
    sample_list2 = [i * 2 for i in range(5000, 10000)]
    concatenated_result = concatenate_lists(sample_list1, sample_list2)
    print(concatenated_result[:5])