class PerfectSquareChecker:
    @staticmethod
    def is_perfect_square(n):
        if n < 0:
            return False
        root = int(n ** 0.5)
        return root * root == n

if __name__ == '__main__':
    checker = PerfectSquareChecker()
    print(checker.is_perfect_square(25))
    print(checker.is_perfect_square(49))
    print(checker.is_perfect_square(18))