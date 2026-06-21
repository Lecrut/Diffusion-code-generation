class TupleSearcher:
    SEARCH_TUPLES = ((1, 2), (3, 4), (5, 6), (7, 8), (9, 10))

    @staticmethod
    def contains_tuple(target):
        return target in TupleSearcher.SEARCH_TUPLES
if __name__ == '__main__':
    sample_tuple = (3, 4)
    result = TupleSearcher.contains_tuple(sample_tuple)
    print(result)