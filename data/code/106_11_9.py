class DateDiffCalculator:
    def __init__(self, date1: str, date2: str):
        self.date1 = date1
        self.date2 = date2

    def _parse_year(self, date_str: str) -> int:
        return int(date_str[0:4])

    def compute_year_difference(self) -> int:
        year1 = self._parse_year(self.date1)
        year2 = self._parse_year(self.date2)
        return abs(year1 - year2)

if __name__ == '__main__':
    calculator = DateDiffCalculator("2020-01-01", "2023-12-31")
    print(calculator.compute_year_difference())
    
    calculator2 = DateDiffCalculator("1999-12-31", "2001-01-01")
    print(calculator2.compute_year_difference())