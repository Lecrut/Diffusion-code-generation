class SequenceAnalyzer:
    def __init__(self, sequence):
        if not sequence:
            raise ValueError('The sequence is empty')
        self.sequence = sequence

    def _calculate_mid_index(self):
        return len(self.sequence) // 2

    def get_central_item(self):
        mid_index = self._calculate_mid_index()
        if len(self.sequence) % 2 == 0:
            return (self.sequence[mid_index - 1] + self.sequence[mid_index]) / 2
        else:
            return self.sequence[mid_index]

if __name__ == '__main__':
    sample_sequence_odd = [3, 6, 9, 12, 15]
    sample_sequence_even = [4, 8, 12, 16, 20, 24]
    
    analyzer_odd = SequenceAnalyzer(sample_sequence_odd)
    analyzer_even = SequenceAnalyzer(sample_sequence_even)
    
    print(analyzer_odd.get_central_item())
    print(analyzer_even.get_central_item())