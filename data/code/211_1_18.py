def jaccard_similarity(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    return len(intersection) / len(union)

if __name__ == '__main__':
    sample_list_a = [10, 20, 30, 40, 50]
    sample_list_b = [40, 50, 60, 70, 80]
    result = jaccard_similarity(sample_list_a, sample_list_b)
    print(result)