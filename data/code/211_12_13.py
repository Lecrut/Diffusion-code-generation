class StringSetComparer:
    def __init__(self, sample1, sample2):
        self.set1 = set(sample1)
        self.set2 = set(sample2)

    def common_elements(self):
        return sorted(list(self.set1 & self.set2))

    def unique_to_set1(self):
        return sorted(list(self.set1 - self.set2))

    def unique_to_set2(self):
        return sorted(list(self.set2 - self.set1))

if __name__ == '__main__':
    comparer = StringSetComparer(
        sample1=['apple', 'banana', 'cherry', 'date'],
        sample2=['banana', 'date', 'fig', 'grape']
    )
    print("Common Elements:", comparer.common_elements())
    print("Unique to Set 1:", comparer.unique_to_set1())
    print("Unique to Set 2:", comparer.unique_to_set2())