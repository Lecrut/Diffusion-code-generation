class TupleCounter:
    @staticmethod
    def count_items(tup):
        count = 0
        for _ in tup:
            count += 1
        return count

if __name__ == '__main__':
    sample_tuple = (1, 2, 3, 4, 5)
    print(TupleCounter.count_items(sample_tuple))