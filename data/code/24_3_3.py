class LeapYearChecker:
    def __init__(self):
        self._divisible_4 = 4
        self._divisible_100 = 100
        self._divisible_400 = 400

    def check(self, year):
        if not isinstance(year, int):
            raise TypeError("Year must be an integer")
        if year <= 0:
            raise ValueError("Year must be a positive integer")
        if year % self._divisible_400 == 0:
            return True
        if year % self._divisible_100 == 0:
            return False
        if year % self._divisible_4 == 0:
            return True
        return False

if __name__ == '__main__':
    checker = LeapYearChecker()
    test_values = [2000, 1900, 2024, 2023, 2400, 2100, 2001, 2012]
    for value in test_values:
        print(checker.check(value))