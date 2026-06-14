import collections
def compare_sets(set1, set2):
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    symmetric_difference = set1.symmetric_difference(set2)
    return intersection, union, symmetric_difference
if __name__ == '__main__':
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}
    intersection_ab, union_ab, symmetric_difference_ab = compare_sets(set_a, set_b)
    print("Set A:", set_a)
    print("Set B:", set_b)
    print("Intersection (A and B):", intersection_ab)
    print("Union (A or B):", union_ab)
    print("Symmetric Difference (A XOR B):", symmetric_difference_ab)