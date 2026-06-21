def concatenate_lists(list1, list2):
    result = list1.copy()
    result.extend(list2)
    return result

if __name__ == '__main__':
    sample_list_a = [1, 2, 3]
    sample_list_b = ['x', 'y', 'z']
    final_result = concatenate_lists(sample_list_a, sample_list_b)
    print(final_result)