class NumberAnalyzer:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate_difference(self):
        return max(self.numbers) - min(self.numbers)

if __name__ == '__main__':
    analyzer = NumberAnalyzer([10, 3, 5, 8])
    result = analyzer.calculate_difference()
    print(result)