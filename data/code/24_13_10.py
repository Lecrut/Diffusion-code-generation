from typing import final

class LeapYearChecker:
    def __init__(self, year: int) -> None:
        self.year = year

    def is_leap_year(self) -> bool:
        year = self.year
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if __name__ == '__main__':
    checker_2000 = LeapYearChecker(2000)
    result_2000 = checker_2000.is_leap_year()
    print(result_2000)

    checker_2023 = LeapYearChecker(2023)
    result_2023 = checker_2023.is_leap_year()
    print(result_2023)

    checker_1900 = LeapYearChecker(1900)
    result_1900 = checker_1900.is_leap_year()
    print(result_1900)