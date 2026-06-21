def find_intersection(list1, list2):
    return list(set(list1) & set(list2))

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [4, 5, 6, 7, 8]
    intersection_result = find_intersection(sample_list1, sample_list2)
    print(intersection_result)

    sample_list3 = ['apple', 'banana', 'cherry']
    sample_list4 = ['banana', 'date', 'elderberry']
    intersection_result2 = find_intersection(sample_list3, sample_list4)
    print(intersection_result2)