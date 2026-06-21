def jaccard_similarity(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    return len(intersection) / len(union)

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4]
    sample_list2 = [3, 4, 5, 6]
    print(jaccard_similarity(sample_list1, sample_list2))