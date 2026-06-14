class SetComparator:
    def analyze(self, set1, set2):
        intersection = set1.intersection(set2)
        union = set1.union(set2)
        difference = set1.difference(set2)
        return (intersection, union, difference)
if __name__ == '__main__':
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}
    comparator = SetComparator()
    result = comparator.analyze(set_a, set_b)
    print(result)