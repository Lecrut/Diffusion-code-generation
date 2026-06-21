def get_intersection(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1 & set2)

if __name__ == '__main__':
    sample_list_x = [10, 20, 30, 40, 50]
    sample_list_y = [30, 40, 50, 60, 70]
    intersection_result = get_intersection(sample_list_x, sample_list_y)
    print(intersection_result)