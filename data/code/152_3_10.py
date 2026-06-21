def find_intersection(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    intersection = set1.intersection(set2)
    return list(intersection)
if __name__ == '__main__':
    sample_list1 = [10, 20, 30, 40, 50]
    sample_list2 = [40, 50, 60, 70, 80]
    result = find_intersection(sample_list1, sample_list2)
    print(result)
    another_sample_list1 = ['red', 'green', 'blue']
    another_sample_list2 = ['green', 'yellow', 'blue']
    another_result = find_intersection(another_sample_list1, another_sample_list2)
    print(another_result)