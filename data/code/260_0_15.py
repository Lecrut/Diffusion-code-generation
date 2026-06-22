class SetComparer:
    def __init__(self, set1, set2):
        self.set1 = set1
        self.set2 = set2

    def find_larger_set(self):
        larger_elements = [x for x in self.set1 if x > max(self.set2)] + \
                         [y for y in self.set2 if y > max(self.set1)]
        return larger_elements

if __name__ == '__main__':
    sample_set1 = {5, 3, 9, 7}
    sample_set2 = {4, 6, 8, 10}
    comparer = SetComparer(sample_set1, sample_set2)
    result = comparer.find_larger_set()
    print(result)