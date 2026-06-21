class StringSetComparer:
    def __init__(self, sample1, sample2):
        self.set1 = set(sample1)
        self.set2 = set(sample2)

    def common_elements(self):
        return sorted(self.set1 & self.set2)

    def unique_entries_in_sample1(self):
        return sorted(self.set1 - self.set2)

    def unique_entries_in_sample2(self):
        return sorted(self.set2 - self.set1)

if __name__ == '__main__':
    comparer = StringSetComparer(sample1=['apple', 'banana', 'cherry'], sample2=['banana', 'date', 'fig'])
    print("Common Elements:", comparer.common_elements())
    print("Unique in Sample 1:", comparer.unique_entries_in_sample1())
    print("Unique in Sample 2:", comparer.unique_entries_in_sample2())