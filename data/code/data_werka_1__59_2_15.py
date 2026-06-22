class SequenceAnalyzer:
    def __init__(self, iterable):
        self.iterable = sorted(iterable)
    
    def get_middle(self):
        n = len(self.iterable)
        if n == 0:
            return None
        middle_index = n // 2
        if n % 2 == 1:
            return self.iterable[middle_index]
        else:
            return (self.iterable[middle_left_index] + self.iterable[middle_right_index]) / 2

if __name__ == '__main__':
    sample_data = [3, 1, 4, 1, 5, 9, 2]
    analyzer = SequenceAnalyzer(sample_data)
    print(analyzer.get_middle())