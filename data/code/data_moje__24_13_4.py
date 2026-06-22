class LeapYearChecker:
    def __init__(self, year: int) -> None:
        self.year: int = year

    def is_leap_year(self) -> bool:
        year: int = self.year
        if year % 4 != 0:
            return False
        if year % 100 != 0:
            return True
        if year % 400 != 0:
            return False
        return True

if __name__ == '__main__':
    checker: LeapYearChecker = LeapYearChecker(2024)
    result: bool = checker.is_leap_year()
    print(result)

    checker2: LeapYearChecker = LeapYearChecker(1900)
    result2: bool = checker2.is_leap_year()
    print(result2)

    checker3: LeapYearChecker = LeapYearChecker(2000)
    result3: bool = checker3.is_leap_year()
    print(result3)

    checker4: LeapYearChecker = LeapYearChecker(2023)
    result4: bool = checker4.is_leap_year()
    print(result4)