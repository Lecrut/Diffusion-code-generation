class MiddleElementFinder:

    def __init__(self, sequence):
        self.sequence = sequence

    def find_middle(self):
        n = len(self.sequence)
        if n == 0:
            raise ValueError('Sequence cannot be empty')
        middle_index = n // 2
        return self.sequence[middle_index]
if __name__ == '__main__':
    sample_sequence1 = [1, 2, 3, 4, 5]
    finder1 = MiddleElementFinder(sample_sequence1)
    print(finder1.find_middle())
    sample_sequence2 = [10, 20, 30, 40, 50, 60, 70]
    finder2 = MiddleElementFinder(sample_sequence2)
    print(finder2.find_middle())
    sample_sequence3 = [1, 2, 3, 4]
    finder3 = MiddleElementFinder(sample_sequence3)
    print(finder3.find_middle())
    sample_sequence4 = [10, 20, 30, 40, 50, 60]
    finder4 = MiddleElementFinder(sample_sequence4)
    print(finder4.find_middle())