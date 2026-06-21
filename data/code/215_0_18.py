class NumberAnalyzer:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_largest(self):
        return max(self.numbers)

if __name__ == '__main__':
    analyzer = NumberAnalyzer([10, 5, 20, 3, 15])
    largest_number = analyzer.find_largest()
    print(largest_number)