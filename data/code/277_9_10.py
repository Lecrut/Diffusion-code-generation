class TupleCounter:
    def __init__(self, data):
        self.data = data

    def count_items(self):
        count = 0
        for _ in self.data:
            count += 1
        return count

if __name__ == '__main__':
    sample_tuple = (1, 2, 3, 4, 5)
    counter = TupleCounter(sample_tuple)
    print(counter.count_items())