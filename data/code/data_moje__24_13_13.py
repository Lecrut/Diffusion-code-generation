class LeapYearChecker:
    def is_leap_year(self, year: int) -> bool:
        if not isinstance(year, int):
            raise TypeError("Year must be an integer")
        if year < 1:
            raise ValueError("Year must be a positive integer")
        if year % 400 == 0:
            return True
        if year % 100 == 0:
            return False
        if year % 4 == 0:
            return True
        return False

if __name__ == '__main__':
    checker = LeapYearChecker()
    print(checker.is_leap_year(2000))
    print(checker.is_leap_year(1900))
    print(checker.is_leap_year(2024))
    print(checker.is_leap_year(2023))