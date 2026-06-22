class SymmetricDifference:
    @staticmethod
    def _to_set(iterable):
        return set(iterable)

    def __init__(self, iterable1, iterable2):
        self.set1 = self._to_set(iterable1)
        self.set2 = self._to_set(iterable2)

    def compute(self):
        return self.set1.symmetric_difference(self.set2)

if __name__ == '__main__':
    list_a = [1, 5, 9]
    list_b = [3, 5, 7]
    symmetric_diff = SymmetricDifference(list_a, list_b)
    result = symmetric_diff.compute()
    print(result)