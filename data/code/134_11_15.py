class OverlapVerifier:
    def has_overlap(self, tuple1, tuple2):
        set1 = set(tuple1)
        set2 = set(tuple2)
        return not set1.isdisjoint(set2)

if __name__ == '__main__':
    verifier = OverlapVerifier()
    sample_tuple1 = (1, 2, 3)
    sample_tuple2 = (4, 5, 6)
    print(f"Tuple 1: {sample_tuple1}, Tuple 2: {sample_tuple2}, Have overlap: {verifier.has_overlap(sample_tuple1, sample_tuple2)}")