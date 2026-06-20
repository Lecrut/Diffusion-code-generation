class PairComparator:
    TRUE_TRUE = (True, True)

    @staticmethod
    def compare_pairs(iterable):
        it = iter(iterable)
        try:
            prev = next(it)
            for curr in it:
                yield prev == curr and curr == True
                prev = curr
        except StopIteration:
            return

if __name__ == '__main__':
    sample_values = [True, False, True, True, False]
    comparator = PairComparator()
    print(list(comparator.compare_pairs(sample_values)))