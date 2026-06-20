class NumberAnalyzer:

    @staticmethod
    def is_even(number):
        return number & 1 == 0
if __name__ == '__main__':
    analyzer = NumberAnalyzer()
    print(analyzer.is_even(4))
    print(analyzer.is_even(7))