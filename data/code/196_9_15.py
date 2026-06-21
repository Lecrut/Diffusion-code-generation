def concatenate_lists(list_x, list_y):
    result = list_x[:]
    result[len(result):] = list_y
    return result

if __name__ == '__main__':
    sample_list1 = [10, 20, 30]
    sample_list2 = [40, 50, 60]
    concatenated_result = concatenate_lists(sample_list1, sample_list2)
    print(concatenated_result)