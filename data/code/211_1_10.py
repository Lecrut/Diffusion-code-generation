def jaccard_similarity(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    intersection_size = len(set1.intersection(set2))
    union_size = len(set1.union(set2))
    return intersection_size / union_size

if __name__ == '__main__':
    list_a = [8, 9, 10, 11, 12]
    list_b = [10, 11, 13, 14, 15]
    similarity = jaccard_similarity(list_a, list_b)
    print(similarity)