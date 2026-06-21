def jaccard_similarity(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    intersection_size = len(set1.intersection(set2))
    union_size = len(set1.union(set2))
    return intersection_size / union_size if union_size != 0 else 0

if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = [4, 5, 6, 7, 8]
    similarity = jaccard_similarity(list_a, list_b)
    print(similarity)