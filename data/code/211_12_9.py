class StringComparator:
    def __init__(self, sample1, sample2):
        self.set1 = set(sample1)
        self.set2 = set(sample2)

    def find_common_elements(self):
        return sorted(list(self.set1 & self.set2))

    def find_unique_entries_in_sample1(self):
        return sorted(list(self.set1 - self.set2))

    def find_unique_entries_in_sample2(self):
        return sorted(list(self.set2 - self.set1))

if __name__ == '__main__':
    comparator = StringComparator(['apple', 'banana', 'cherry'], ['banana', 'date', 'fig'])
    print("Common elements:", comparator.find_common_elements())
    print("Unique entries in sample 1:", comparator.find_unique_entries_in_sample1())
    print("Unique entries in sample 2:", comparator.find_unique_entries_in_sample2())