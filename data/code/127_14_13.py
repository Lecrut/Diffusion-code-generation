class NumberAnalyzer:
    def is_odd(self, n):
        return n & 1

if __name__ == '__main__':
    analyzer = NumberAnalyzer()
    print(f"Is 4 odd? {analyzer.is_odd(4)}")
    print(f"Is 7 odd? {analyzer.is_odd(7)}")
    print(f"Is 0 odd? {analyzer.is_odd(0)}")