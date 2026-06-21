class NumberAnalyzer:

    def __init__(self, number):
        self.number = number

    def is_perfect_square(self):
        if self.number < 0:
            return False
        root = int(self.number ** 0.5)
        return root * root == self.number
if __name__ == '__main__':
    analyzer1 = NumberAnalyzer(25)
    print(analyzer1.is_perfect_square())
    analyzer2 = NumberAnalyzer(14)
    print(analyzer2.is_perfect_square())