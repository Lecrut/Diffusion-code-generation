class NumberAnalyzer:
    @staticmethod
    def is_odd(n):
        return n & 1

if __name__ == '__main__':
    analyzer = NumberAnalyzer()
    print(f"Is 4 odd? {analyzer.is_odd(4)}")
    print(f"Is 5 odd? {analyzer.is_odd(5)}")
    print(f"Is 0 odd? {analyzer.is_odd(0)}")