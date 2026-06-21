def merge_lists(list_x, list_y):
    result_list = []
    for element in list_x:
        result_list.append(element)
    list_y.extend(result_list)
    return list_y

if __name__ == '__main__':
    sample_list1 = [10, 20, 30]
    sample_list2 = [40, 50]
    merged_list = merge_lists(sample_list1, sample_list2)
    print(merged_list)