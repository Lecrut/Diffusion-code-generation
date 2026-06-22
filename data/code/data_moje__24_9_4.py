class LeapYearChecker:
    MOD_4 = 4
    MOD_100 = 100
    MOD_400 = 400

    @staticmethod
    def _is_divisible(value, divisor):
        return value % divisor == 0

    def check(self, year):
        if self._is_divisible(year, self.MOD_400):
            return True
        if self._is_divisible(year, self.MOD_100):
            return False
        return self._is_divisible(year, self.MOD_4)

if __name__ == '__main__':
    checker = LeapYearChecker()
    print(checker.check(2000))
    print(checker.check(1900))
    print(checker.check(2024))
    print(checker.check(2023))
    print(checker.check(2004))