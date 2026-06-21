class TupleExtender:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def extend_tuples(self):
        return self.list1 + self.list2

if __name__ == '__main__':
    sample_list1 = [(1, 2), (3, 4)]
    sample_list2 = [(5, 6), (7, 8)]
    extender = TupleExtender(sample_list1, sample_list2)
    result = extender.extend_tuples()
    print(result)