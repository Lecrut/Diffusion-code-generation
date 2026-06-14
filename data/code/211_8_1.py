import sys
def compare_sets(set1, set2):
    print("--- Set Comparison Report ---")
    print(f"Set 1: {sorted(list(set1))}")
    print(f"Set 2: {sorted(list(set2))}")
    print("\n--- Set Operations ---")
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    difference_1_2 = set1.difference(set2)
    difference_2_1 = set2.difference(set1)
    symmetric_difference = set1.symmetric_difference(set2)
    print(f"Intersection (Set1 & Set2): {sorted(list(intersection))}")
    print(f"Union (Set1 | Set2): {sorted(list(union))}")
    print(f"Difference (Set1 - Set2): {sorted(list(difference_1_2))}")
    print(f"Difference (Set2 - Set1): {sorted(list(difference_2_1))}")
    print(f"Symmetric Difference (Set1 ^ Set2): {sorted(list(symmetric_difference))}")
if __name__ == '__main__':
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}
    compare_sets(set_a, set_b)