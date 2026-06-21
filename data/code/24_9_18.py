class LeapYearChecker:
    def __init__(self):
        self._div_4 = 4
        self._div_100 = 100
        self._div_400 = 400

    def check(self, year):
        is_divisible_by_4 = year % self._div_4 == 0
        is_divisible_by_100 = year % self._div_100 == 0
        is_divisible_by_400 = year % self._div_400 == 0
        
        if is_divisible_by_400:
            return True
        if is_divisible_by_100:
            return False
        return is_divisible_by_4

if __name__ == '__main__':
    checker = LeapYearChecker()
    print(checker.check(2000))
    print(checker.check(1900))
    print(checker.check(2024))
    print(checker.check(2023))
    print(checker.check(2004))
    print(checker.check(1800))