def extend_lists(list1, list2):
    result = list1.copy()
    result.extend(list2)
    return result

if __name__ == '__main__':
    sample_list_x = [10, 20, 30]
    sample_list_y = [40, 50, 60]
    concatenated_list = extend_lists(sample_list_x, sample_list_y)
    print(concatenated_list)