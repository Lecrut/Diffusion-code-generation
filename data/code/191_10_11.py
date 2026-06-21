def extend_list_with_copy(list1, list2):
    result = list1.copy()
    result.extend(list2)
    return result

if __name__ == '__main__':
    sample_list_a = ['a', 'b', 'c']
    sample_list_b = ['d', 'e', 'f']
    combined_result = extend_list_with_copy(sample_list_a, sample_list_b)
    print(combined_result)