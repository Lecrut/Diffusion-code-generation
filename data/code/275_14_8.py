class TupleCounter:
    def __init__(self):
        self.counts = {}

    def add_tuple(self, t):
        if t[0] in self.counts:
            self.counts[t[0]] += 1
        else:
            self.counts[t[0]] = 1

    def get_counts(self):
        return self.counts

if __name__ == '__main__':
    counter = TupleCounter()
    sample_tuples = ((1, 'a'), (2, 'b'), (1, 'c'), (3, 'd'), (2, 'e'))
    for t in sample_tuples:
        counter.add_tuple(t)
    print(counter.get_counts())