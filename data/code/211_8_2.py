import sys
def compare_sets(set1, set2):
    print("--- Set Comparison Report ---")
    print(f"Set 1: {set1}")
    print(f"Set 2: {set2}")
    print("\n--- Basic Set Operations ---")
    print(f"Union (Set1 | Set2): {set1.union(set2)}")
    print(f"Intersection (Set1 & Set2): {set1.intersection(set2)}")
    print(f"Difference (Set1 - Set2): {set1.difference(set2)}")
    print(f"Difference (Set2 - Set1): {set2.difference(set1)}")
    print(f"Symmetric Difference (Set1 ^ Set2): {set1.symmetric_difference(set2)}")
    print("\n--- Set Subset/Superset Relations ---")
    print(f"Is Set1 a subset of Set2? ({set1} <= {set2}): {set1.issubset(set2)}")
    print(f"Is Set2 a subset of Set1? ({set2} <= {set1}): {set2.issubset(set1)}")
    print(f"Is Set1 a superset of Set2? ({set1} >= {set2}): {set1.issuperset(set2)}")
    print(f"Is Set2 a superset of Set1? ({set2} >= {set1}): {set2.issuperset(set1)}")
    print("\n--- Set Size Comparison ---")
    print(f"Size of Set 1: {len(set1)}")
    print(f"Size of Set 2: {len(set2)}")
if __name__ == '__main__':
    sample_set_a = {1, 2, 3, 4, 5}
    sample_set_b = {4, 5, 6, 7, 8}
    compare_sets(sample_set_a, sample_set_b)