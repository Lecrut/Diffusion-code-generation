class NumberAnalyzer:
    def is_odd(self, n):
        return n & 1 == 1

if __name__ == '__main__':
    analyzer = NumberAnalyzer()
    print(analyzer.is_odd(3))
    print(analyzer.is_odd(4))