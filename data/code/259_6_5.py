class NumberAnalyzer:
    def __init__(self, numbers_str):
        self.numbers = [int(num) for num in numbers_str.split(',')]

    def find_extremes(self):
        smallest = min(self.numbers)
        largest = max(self.numbers)
        return smallest, largest

if __name__ == '__main__':
    analyzer = NumberAnalyzer("3,1,4,1,5,9,2,6,5,3,5")
    min_val, max_val = analyzer.find_extremes()
    print(f"Minimum: {min_val}, Maximum: {max_val}")