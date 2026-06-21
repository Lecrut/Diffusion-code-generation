class TupleExtender:
    def __init__(self):
        self.sample_list1 = [(1, 2), (3, 4)]
        self.sample_list2 = [(5, 6), (7, 8)]

    def extend_tuples(self):
        return self.sample_list1 + self.sample_list2

if __name__ == '__main__':
    extender = TupleExtender()
    result = extender.extend_tuples()
    print(result)