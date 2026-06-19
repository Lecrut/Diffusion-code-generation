class MiddleFinder:
    def __init__(self, sequence):
        self.sequence = sequence

    def find_middle(self):
        if not self.sequence:
            return None
        n = len(self.sequence)
        middle_index = n // 2
        return self.sequence[middle_index]

if __name__ == '__main__':
    sample_input = [10, 20, 30, 40, 50]
    finder = MiddleFinder(sample_input)
    print(finder.find_middle())