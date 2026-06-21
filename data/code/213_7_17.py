class NumberAnalyzer:
    def is_perfect_square(self, n):
        if n < 0:
            return False
        root = int(n ** 0.5)
        return root * root == n

if __name__ == '__main__':
    analyzer = NumberAnalyzer()
    print(analyzer.is_perfect_square(16))
    print(analyzer.is_perfect_square(14))