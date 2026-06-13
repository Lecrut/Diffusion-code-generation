class SetComparator:
    def compare_sets(self, set1, set2):
        length_comparison = len(set1) - len(set2)
        return (set1, set2, length_comparison)
if __name__ == '__main__':
    comparator = SetComparator()
    set_a = {1, 2, 3}
    set_b = {3, 4, 5}
    result = comparator.compare_sets(set_a, set_b)
    print(result)