def concatenate_lists(list_x, list_y):
    result = list_x[:]
    result[len(result):] = list_y
    return result

if __name__ == '__main__':
    sample_list1 = [7, 8, 9]
    sample_list2 = [10, 11, 12]
    print(concatenate_lists(sample_list1, sample_list2))