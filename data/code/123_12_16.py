class FloatTupleSum:
    @staticmethod
    def calculate_sum(float_tuple):
        return sum(float_tuple)

if __name__ == '__main__':
    sample_tuple = (1.5, 2.3, 3.7)
    result = FloatTupleSum.calculate_sum(sample_tuple)
    print(f"Sum of {sample_tuple}: {result}")