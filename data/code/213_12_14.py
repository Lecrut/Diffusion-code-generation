class SetOperations:
    def calculate_intersection(self, set1, set2):
        return set1.intersection(set2)

    def calculate_union(self, set1, set2):
        return set1.union(set2)

    def calculate_difference(self, set1, set2):
        return set1.difference(set2)

if __name__ == '__main__':
    analyzer = SetOperations()
    sample_set1 = {1, 2, 3, 4, 5}
    sample_set2 = {4, 5, 6, 7, 8}

    intersection_result = analyzer.calculate_intersection(sample_set1, sample_set2)
    union_result = analyzer.calculate_union(sample_set1, sample_set2)
    difference_result = analyzer.calculate_difference(sample_set1, sample_set2)

    print("Intersection:", intersection_result)
    print("Union:", union_result)
    print("Difference:", difference_result)