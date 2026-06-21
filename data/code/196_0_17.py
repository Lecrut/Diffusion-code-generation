def concatenate_lists(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Both inputs must be lists.")
    
    result = list1.copy()
    result.extend(list2)
    return result

if __name__ == '__main__':
    sample_list1 = [i for i in range(1000000)]
    sample_list2 = [i for i in range(1000000, 2000000)]
    concatenated_result = concatenate_lists(sample_list1, sample_list2)
    print(concatenated_result[:5])