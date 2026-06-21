class MiddleElementGenerator:
    def __init__(self, sequence):
        self.sequence = sequence

    def _is_odd_length(self):
        return len(self.sequence) % 2 == 1

    def generate_middle_elements(self):
        length = len(self.sequence)
        if not self.sequence:
            raise ValueError("The sequence is empty")
        
        mid_index = length // 2
        if self._is_odd_length():
            yield self.sequence[mid_index]
        else:
            yield self.sequence[mid_index - 1]
            yield self.sequence[mid_index]

if __name__ == '__main__':
    sample_sequence_odd = [1, 2, 3, 4, 5]
    sample_sequence_even = [1, 2, 3, 4, 5, 6]

    print("Middle elements of odd-length sequence:")
    try:
        for middle in MiddleElementGenerator(sample_sequence_odd).generate_middle_elements():
            print(middle)
    except ValueError as e:
        print(e)

    print("\nMiddle elements of even-length sequence:")
    try:
        for middle in MiddleElementGenerator(sample_sequence_even).generate_middle_elements():
            print(middle)
    except ValueError as e:
        print(e)