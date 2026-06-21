class NumberAnalyzer:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_largest(self):
        return max(self.numbers)

if __name__ == '__main__':
    analyzer = NumberAnalyzer([3.5, 2.1, 4.8, 1.9, 5.6])
    largest_number = analyzer.find_largest()
    print(largest_number)