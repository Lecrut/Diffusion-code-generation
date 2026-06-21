class NumberChecker:
    MIN_COUNT = 3
    DIVISOR = 2

    @staticmethod
    def _is_valid(num):
        return num > 0 and num % NumberChecker.DIVISOR == 0

    def check(self, numbers):
        valid_count = 0
        for num in numbers:
            if self._is_valid(num):
                valid_count += 1
        return valid_count >= NumberChecker.MIN_COUNT

if __name__ == '__main__':
    checker = NumberChecker()
    data1 = [2, 4, 6, 1, 3, 5]
    data2 = [1, 3, 5, 7, 9]
    data3 = [2, 4, 6, 8, 10]
    data4 = [10, 20, 30, 40]
    print(checker.check(data1))
    print(checker.check(data2))
    print(checker.check(data3))
    print(checker.check(data4))