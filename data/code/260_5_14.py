class MaxTupleCalculator:
    @staticmethod
    def max_tuples(tuple1, tuple2):
        return tuple(max(a, b) for a, b in zip(tuple1, tuple2))

if __name__ == '__main__':
    sample_tuple1 = (1, 3, 5, 7, 9)
    sample_tuple2 = (0, 2, 4, 6, 8)
    result = MaxTupleCalculator.max_tuples(sample_tuple1, sample_tuple2)
    print(result)