class SequenceFinder:
    def __init__(self, sequence):
        self.sequence = sequence

    def find_middle_item(self):
        length = len(self.sequence)
        if length == 0:
            raise ValueError("The sequence is empty")
        middle_index = length // 2
        return self.sequence[middle_index]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    finder = SequenceFinder(sample_list)
    print(finder.find_middle_item())

    another_sample_list = [10, 20, 30, 40, 50]
    another_finder = SequenceFinder(another_sample_list)
    print(another_finder.find_middle_item())