class ThreeNumberAnalyzer:
    def __init__(self, a, b, c):
        self.numbers = [a, b, c]
    def find_middle(self):
        self.numbers.sort()
        return self.numbers[1]
if __name__ == '__main__':
    analyzer = ThreeNumberAnalyzer(10, 5, 20)
    middle = analyzer.find_middle()
    print(middle)