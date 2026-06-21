class SetComparer:
    def __init__(self, set1, set2):
        self.set1 = set1
        self.set2 = set2

    def get_unique_and_common(self):
        unique_to_set1 = self.set1 - self.set2
        unique_to_set2 = self.set2 - self.set1
        common_elements = self.set1 & self.set2
        return (unique_to_set1, unique_to_set2, common_elements)

if __name__ == '__main__':
    comparer = SetComparer({1, 2, 3, 4}, {3, 4, 5, 6})
    unique_a, unique_b, common = comparer.get_unique_and_common()
    print("Unique to set 1:", unique_a)
    print("Unique to set 2:", unique_b)
    print("Common elements:", common)