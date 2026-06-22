def find_distinct_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1 - set2)

if __name__ == '__main__':
    sample_list_a = [10, 20, 30, 40, 50]
    sample_list_b = [30, 40, 60, 70, 80]
    distinct_elements = find_distinct_elements(sample_list_a, sample_list_b)
    print(distinct_elements)