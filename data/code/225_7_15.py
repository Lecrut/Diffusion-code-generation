class ValueComparer:
    def __init__(self, tuple1, tuple2):
        self.values = tuple1 + tuple2

    def get_min(self):
        return min(self.values)

    def get_max(self):
        return max(self.values)

if __name__ == '__main__':
    sample_tuple1 = (5, 9, 3)
    sample_tuple2 = (7, 1, 8)
    comparer = ValueComparer(sample_tuple1, sample_tuple2)
    print(f"Tuple 1: {sample_tuple1}")
    print(f"Tuple 2: {sample_tuple2}")
    print(f"Minimum value: {comparer.get_min()}")
    print(f"Maximum value: {comparer.get_max()}")