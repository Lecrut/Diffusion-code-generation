class SequenceAnalyzer:
    def __init__(self, sequence):
        self.sequence = sequence

    def find_middle_index(self):
        length = len(self.sequence)
        return (length - 1) // 2

if __name__ == '__main__':
    odd_sequence = [1.0, 2.0, 3.0, 4.0, 5.0]
    even_sequence = [1.0, 2.0, 3.0, 4.0]

    analyzer_odd = SequenceAnalyzer(odd_sequence)
    analyzer_even = SequenceAnalyzer(even_sequence)

    print("Middle index of odd sequence:", analyzer_odd.find_middle_index())
    print("Middle index of even sequence:", analyzer_even.find_middle_index())