import sys
def compare_string_sets(set1, set2):
    if set1 == set2:
        return "Identical", 0, 0
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    return "Not Identical", len(intersection), len(union)
if __name__ == '__main__':
    set_a = {"apple", "banana", "cherry", "date"}
    set_b = {"banana", "cherry", "elderberry", "fig"}
    status, intersection_size, union_size = compare_string_sets(set_a, set_b)
    print(f"Comparison Status: {status}")
    print(f"Intersection Size: {intersection_size}")
    print(f"Union Size: {union_size}")