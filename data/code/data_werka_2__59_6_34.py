class SequenceMiddleFinder:
    def __init__(self, sequence):
        self.sequence = sequence

    def middle_elements(self):
        length = len(self.sequence)
        if length == 0:
            raise ValueError("The sequence is empty")
        
        mid_index = length // 2
        if length % 2 == 1:
            yield self.sequence[mid_index]
        else:
            yield self.sequence[mid_index - 1]
            yield self.sequence[mid_index]

if __name__ == '__main__':
    sample_sequence_odd = [10, 20, 30, 40, 50]
    sample_sequence_even = [10, 20, 30, 40, 50, 60]

    finder_odd = SequenceMiddleFinder(sample_sequence_odd)
    print("Middle elements of odd-length sequence:")
    for middle in finder_odd.middle_elements():
        print(middle)

    finder_even = SequenceMiddleFinder(sample_sequence_even)
    print("Middle elements of even-length sequence:")
    for middle in finder_even.middle_elements():
        print(middle)