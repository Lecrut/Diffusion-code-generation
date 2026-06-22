class MiddleElementFinder:

    def __init__(self, sequence):
        self.sequence = sequence

    @staticmethod
    def calculate_middle_index(length):
        return (length - 1) // 2

    def find_middle_item(self):
        if not self.sequence:
            return None
        middle_index = self.calculate_middle_index(len(self.sequence))
        return self.sequence[middle_index]
if __name__ == '__main__':
    sample_sequence_odd = list(range(1, 11))
    sample_sequence_even = list(range(1, 12))
    finder_odd = MiddleElementFinder(sample_sequence_odd)
    finder_even = MiddleElementFinder(sample_sequence_even)
    print(finder_odd.find_middle_item())
    print(finder_even.find_middle_item())