class PairComparator:
    TRUE_TRUE = (True, True)

    @staticmethod
    def compare_pairs(iterable):
        it = iter(iterable)
        prev = next(it, None)
        for curr in it:
            yield (prev, curr) == PairComparator.TRUE_TRUE
            prev = curr

if __name__ == '__main__':
    sample_values = [True, False, True, True, False]
    print(list(PairComparator.compare_pairs(sample_values)))