def concatenate_lists(list1, list2):
    result = list1.copy()
    result.extend(list2)
    return result

if __name__ == '__main__':
    sample_list1 = [i for i in range(500000)]
    sample_list2 = [chr(i) for i in range(65, 65+26)]
    concatenated_result = concatenate_lists(sample_list1, sample_list2)
    print(concatenated_result[:10])