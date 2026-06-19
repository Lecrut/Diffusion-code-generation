class SequenceAnalyzer:
    def __init__(self, sequence):
        self.sequence = sequence

    def get_central_item(self):
        if not self.sequence:
            return None
        length = len(self.sequence)
        mid_index = length // 2
        if length % 2 == 0:
            return (self.sequence[mid_index - 1], self.sequence[mid_index])
        else:
            return self.sequence[mid_index]

if __name__ == '__main__':
    sample_sequence_1 = [1, 2, 3, 4, 5]
    sample_sequence_2 = [10, 20, 30, 40]
    sample_sequence_3 = []

    analyzer_1 = SequenceAnalyzer(sample_sequence_1)
    analyzer_2 = SequenceAnalyzer(sample_sequence_2)
    analyzer_3 = SequenceAnalyzer(sample_sequence_3)

    print(analyzer_1.get_central_item())
    print(analyzer_2.get_central_item())
    print(analyzer_3.get_central_item())