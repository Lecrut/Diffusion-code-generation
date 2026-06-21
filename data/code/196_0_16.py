def concatenate_lists(list1, list2):
    result = list1.copy()
    result.extend(list2)
    return result

if __name__ == '__main__':
    sample_list_a = [i for i in range(5000)]
    sample_list_b = [chr(i) for i in range(65, 100)]
    concatenated_result = concatenate_lists(sample_list_a, sample_list_b)
    print(concatenated_result[:5])