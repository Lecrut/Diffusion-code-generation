class CentralItemFinder:
    def __init__(self, sequence):
        if not sequence:
            raise ValueError('The sequence is empty')
        self.sequence = sequence

    def get_central_item(self):
        length = len(self.sequence)
        mid_index = length // 2
        if length % 2 == 0:
            return (self.sequence[mid_index - 1] + self.sequence[mid_index]) / 2
        else:
            return self.sequence[mid_index]

if __name__ == '__main__':
    sample_sequence_odd = [1, 3, 5, 7, 9]
    sample_sequence_even = [2, 4, 6, 8, 10, 12]

    finder_odd = CentralItemFinder(sample_sequence_odd)
    finder_even = CentralItemFinder(sample_sequence_even)

    print(finder_odd.get_central_item())
    print(finder_even.get_central_item())