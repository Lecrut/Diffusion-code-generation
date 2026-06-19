class AbsoluteDifferenceIterator:

    def __init__(self, list1, list2):
        if len(list1) != len(list2):
            raise ValueError('Both lists must have the same length.')
        self.list1 = list1
        self.list2 = list2
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.list1):
            diff = abs(self.list1[self.index] - self.list2[self.index])
            self.index += 1
            return diff
        else:
            raise StopIteration
if __name__ == '__main__':
    list_a = [8, 16, 24, 32]
    list_b = [4, 8, 12, 16]
    iterator = AbsoluteDifferenceIterator(list_a, list_b)
    for diff in iterator:
        print(diff)
    list_c = [50, 75, 100]
    list_d = [40, 60, 80]
    iterator.list1 = list_c
    iterator.list2 = list_d
    for diff in iterator:
        print(diff)