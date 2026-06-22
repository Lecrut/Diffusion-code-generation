class NumberChecker:
    MIN_COUNT = 3
    DIVISOR = 2

    @staticmethod
    def _is_valid(num):
        return num > 0 and num % NumberChecker.DIVISOR == 0

    @classmethod
    def check(cls, numbers):
        valid_count = 0
        for num in numbers:
            if cls._is_valid(num):
                valid_count += 1
        return valid_count >= cls.MIN_COUNT

if __name__ == '__main__':
    data_a = [2, 4, 6, 1, 3, 5]
    data_b = [1, 3, 5, 7, 9]
    data_c = [2, 4, 6, 8, 10]
    data_d = [10, 20, 30]
    
    print(NumberChecker.check(data_a))
    print(NumberChecker.check(data_b))
    print(NumberChecker.check(data_c))
    print(NumberChecker.check(data_d))