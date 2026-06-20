class NumberAnalyzer:
    def __init__(self, number):
        self.number = number

    def is_odd(self):
        return self.number % 2 != 0

if __name__ == '__main__':
    analyzer1 = NumberAnalyzer(4)
    print(f"{analyzer1.number} is odd: {analyzer1.is_odd()}")

    analyzer2 = NumberAnalyzer(7)
    print(f"{analyzer2.number} is odd: {analyzer2.is_odd()}")

    analyzer3 = NumberAnalyzer(0)
    print(f"{analyzer3.number} is odd: {analyzer3.is_odd()}")

    analyzer4 = NumberAnalyzer(-3)
    print(f"{analyzer4.number} is odd: {analyzer4.is_odd()}")