class SequenceAnalyzer:
    def __init__(self, iterable):
        self.iterable = sorted(iterable)

    def get_middle(self):
        length = len(self.iterable)
        if length == 0:
            raise ValueError("Input is empty")
        middle_index = length // 2
        if length % 2 == 1:
            return self.iterable[middle_index]
        else:
            return (self.iterable[middle_index - 1] + self.iterable[middle_index]) / 2

if __name__ == '__main__':
    sample_input = [5, 3, 8, 1, 4]
    analyzer = SequenceAnalyzer(sample_input)
    middle_value = analyzer.get_middle()
    print(middle_value)