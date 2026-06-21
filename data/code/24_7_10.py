class LeapYearChecker:
    RULES = {400: 0, 100: 1, 4: 1}

    def __init__(self, year):
        if not isinstance(year, int):
            raise TypeError("Year must be an integer")
        if year < 1:
            raise ValueError("Year must be positive")
        self.year = year

    def is_leap(self):
        year = self.year
        for divisor, result in self.RULES.items():
            if year % divisor == 0:
                return result == 0
        return False

if __name__ == '__main__':
    checker_2000 = LeapYearChecker(2000)
    checker_1900 = LeapYearChecker(1900)
    checker_2024 = LeapYearChecker(2024)
    checker_2023 = LeapYearChecker(2023)
    
    print(checker_2000.is_leap())
    print(checker_1900.is_leap())
    print(checker_2024.is_leap())
    print(checker_2023.is_leap())