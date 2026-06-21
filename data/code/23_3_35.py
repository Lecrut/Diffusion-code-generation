class ValueComparator:
    def __init__(self, seq1, seq2):
        self.seq1 = seq1
        self.seq2 = seq2

    def compare(self):
        for a, b in zip(self.seq1, self.seq2):
            if a > b:
                yield f'{a} is greater'
            elif a < b:
                yield f'{b} is smaller'
            else:
                yield 'Equal'

if __name__ == '__main__':
    sequence1 = [7, 2, 5, 8]
    sequence2 = [6, 3, 5, 7]
    comparator = ValueComparator(sequence1, sequence2)
    for result in comparator.compare():
        print(result)