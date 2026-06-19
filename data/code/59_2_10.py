class SequenceAnalyzer:
    def __init__(self, iterable):
        self.iterable = sorted(iterable)

    def get_middle(self):
        n = len(self.iterable)
        if n % 2 == 1:
            return self.iterable[n // 2]
        else:
            middle_left_index = n // 2 - 1
            middle_right_index = n // 2
            return (self.iterable[middle_left_index] + self.iterable[middle_right_index]) / 2

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    analyzer = SequenceAnalyzer(sample_values)
    print(analyzer.get_middle())