class InvalidLengthException(Exception):
    def __init__(self, text):
        super().__init__(text)
        self.error_text = text

class PairAnalyzer:
    def __init__(self, a, b):
        self.side_a = a
        self.side_b = b

    def validate_and_compute_sum(self):
        if self.side_a < 0 or self.side_b < 0:
            raise InvalidLengthException("Lengths must be non-negative")
        return self.side_a + self.side_b

if __name__ == '__main__':
    analyzer = PairAnalyzer(5, 10)
    total = analyzer.validate_and_compute_sum()
    print(total)