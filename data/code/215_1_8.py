class TupleAnalyzer:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_largest(self):
        return max(self.numbers)

if __name__ == '__main__':
    analyzer = TupleAnalyzer((99, 45, 67, 12, 88))
    largest_number = analyzer.find_largest()
    print(largest_number)