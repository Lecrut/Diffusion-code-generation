class SetComparer:
    def __init__(self, set1, set2):
        self.set1 = set1
        self.set2 = set2

    def compare(self):
        unique_to_set1 = self.set1 - self.set2
        unique_to_set2 = self.set2 - self.set1
        common_elements = self.set1 & self.set2
        return (unique_to_set1, unique_to_set2, common_elements)

if __name__ == '__main__':
    comparer = SetComparer({1, 2, 3, 4}, {3, 4, 5, 6})
    result = comparer.compare()
    print(result)