class DayOfWeekCalculator:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def _is_leap_year(self, y):
        return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

    def _days_in_month(self, y, m):
        if m == 2:
            return 29 if self._is_leap_year(y) else 28
        if m in (4, 6, 9, 11):
            return 30
        return 31

    def calculate(self):
        y = self.year
        m = self.month
        d = self.day
        if m < 3:
            y -= 1
            m += 12
        k = y % 100
        j = y // 100
        h = (d + (13 * (m + 1)) // 5 + k + k // 4 + j // 4 + 5 * j) % 7
        names = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        return names[h]

    def is_valid(self):
        if self.month < 1 or self.month > 12:
            return False
        if self.day < 1:
            return False
        return self.day <= self._days_in_month(self.year, self.month)

if __name__ == '__main__':
    calc = DayOfWeekCalculator(2024, 2, 29)
    print(calc.calculate())
    print(calc.is_valid())
    calc2 = DayOfWeekCalculator(2000, 2, 29)
    print(calc2.calculate())
    print(calc2.is_valid())