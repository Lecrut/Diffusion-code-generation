class ArrayComparer:

    def __init__(self, array1, array2):
        self.array1 = array1
        self.array2 = array2

    def count_matching_elements(self, position):
        return sum((1 for a, b in zip(self.array1, self.array2) if a == b and a == position))
if __name__ == '__main__':
    comparer = ArrayComparer([1, 2, 3, 4, 5], [1, 2, 4, 4, 6])
    print(comparer.count_matching_elements(1))
    print(comparer.count_matching_elements(4))