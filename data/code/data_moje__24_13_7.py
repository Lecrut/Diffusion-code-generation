class LeapYearChecker:
    def __init__(self, year: int) -> None:
        self.year = year

    def is_leap_year(self) -> bool:
        if self.year % 4 != 0:
            return False
        if self.year % 100 != 0:
            return True
        if self.year % 400 != 0:
            return False
        return True

if __name__ == '__main__':
    years_to_check = [2000, 1900, 2024, 2023, 2400, 1800]
    results = []
    for y in years_to_check:
        checker = LeapYearChecker(y)
        results.append((y, checker.is_leap_year()))
    for year, is_leap in results:
        print(f"{year}: {is_leap}")