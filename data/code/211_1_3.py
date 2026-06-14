class SetComparator:
    def compare_sets(self, list1, list2):
        set1 = set(list1)
        set2 = set(list2)
        intersection = set1.intersection(set2)
        union = set1.union(set2)
        difference1 = set1.difference(set2)
        difference2 = set2.difference(set1)
        return {
            "intersection_size": len(intersection),
            "union_size": len(union),
            "difference_list1_only_size": len(difference1),
            "difference_list2_only_size": len(difference2)
        }
if __name__ == '__main__':
    comparator = SetComparator()
    list_a = [1, 2, 3, 4, 5]
    list_b = [4, 5, 6, 7, 8]
    results = comparator.compare_sets(list_a, list_b)
    print(results)