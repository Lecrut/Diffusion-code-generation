class MiddleElementFinder:

    def __init__(self, sequence):
        self.sequence = sequence

    @staticmethod
    def _validate_sequence(sequence):
        if not sequence:
            raise ValueError('Sequence cannot be empty')

    @staticmethod
    def _calculate_middle_index(length):
        return length // 2

    def find_middle(self):
        self._validate_sequence(self.sequence)
        middle_index = self._calculate_middle_index(len(self.sequence))
        return self.sequence[middle_index]
if __name__ == '__main__':
    sample_sequence_odd = [1, 2, 3, 4, 5]
    sample_sequence_even = [10, 20, 30, 40, 50, 60]
    finder_odd = MiddleElementFinder(sample_sequence_odd)
    finder_even = MiddleElementFinder(sample_sequence_even)
    print(finder_odd.find_middle())
    print(finder_even.find_middle())