class TupleChecker:
    def __init__(self, tuple_list):
        self.tuple_list = tuple_list

    def contains_tuple(self, target_tuple):
        return target_tuple in self.tuple_list

if __name__ == '__main__':
    checker = TupleChecker([
        (1, 2), (3, 4), (5, 6), (7, 8)
    ])
    
    print(checker.contains_tuple((3, 4)))
    print(checker.contains_tuple((9, 0)))