class NumberAnalyzer:
    @staticmethod
    def is_perfect_square(n):
        if n < 0:
            return False
        root = int(n ** 0.5)
        return root * root == n

if __name__ == '__main__':
    print(NumberAnalyzer.is_perfect_square(16))
    print(NumberAnalyzer.is_perfect_square(14))