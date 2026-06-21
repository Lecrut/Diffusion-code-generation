def validate_lists(list1, list2):
    if not all(isinstance(x, int) for x in list1 + list2):
        raise ValueError("Both lists must contain only integers.")
    return set(list1), set(list2)

def jaccard_similarity(set1, set2):
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    if len(union) == 0:
        return 0.0
    return len(intersection) / len(union)

if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = [4, 5, 6, 7, 8]
    set_a, set_b = validate_lists(list_a, list_b)
    similarity = jaccard_similarity(set_a, set_b)
    print(similarity)