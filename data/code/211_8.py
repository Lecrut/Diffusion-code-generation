import sys
def compare_sets(set1, set2):
    comparison = {}
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    difference1 = set1.difference(set2)
    difference2 = set2.difference(set1)
    symmetric_difference = set1.symmetric_difference(set2)
    comparison['Set 1'] = sorted(list(set1))
    comparison['Set 2'] = sorted(list(set2))
    comparison['Intersection'] = sorted(list(intersection))
    comparison['Union'] = sorted(list(union))
    comparison['Difference (Set 1 - Set 2)'] = sorted(list(difference1))
    comparison['Difference (Set 2 - Set 1)'] = sorted(list(difference2))
    comparison['Symmetric Difference'] = sorted(list(symmetric_difference))
    return comparison
if __name__ == '__main__':
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}
    report = compare_sets(set_a, set_b)
    print("--- Set Comparison Report ---")
    for key, value in report.items():
        print(f"{key}: {value}")