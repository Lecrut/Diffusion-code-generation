class SequenceSorter:
    def __init__(self, values):
        self.values = values

    def sort_and_print(self):
        sorted_sequence = sorted(self.values, key=lambda x: x)
        print(sorted_sequence)

if __name__ == '__main__':
    sorter = SequenceSorter([10, 5, 20])
    sorter.sort_and_print()