def find_intersection(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    intersection = [item for item in set1 if item in set2]
    return intersection

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [4, 5, 6, 7, 8]
    result = find_intersection(sample_list1, sample_list2)
    print(f"Intersection of {sample_list1} and {sample_list2}: {result}")