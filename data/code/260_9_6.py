class SetMerger:
    def merge_and_sort(self, set1, set2):
        return sorted(set1.union(set2))

if __name__ == '__main__':
    merger = SetMerger()
    sample_set1 = {3, 1, 4}
    sample_set2 = {2, 5, 6}
    result = merger.merge_and_sort(sample_set1, sample_set2)
    print(result)