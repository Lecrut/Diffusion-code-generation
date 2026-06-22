class DateCalculator:
    def __init__(self, year, month, day):
        if not (1 <= month <= 12):
            raise ValueError("Invalid month")
        if not (1 <= day <= 31):
            raise ValueError("Invalid day")
        self.year = year
        self.month = month
        self.day = day

    def _is_leap(self, y):
        return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

    def _days_in_month(self, m, y):
        if m == 2:
            return 29 if self._is_leap(y) else 28
        if m in (4, 6, 9, 11):
            return 30
        return 31

    def _total_days_from_epoch(self):
        days = 0
        for y in range(1, self.year):
            days += 366 if self._is_leap(y) else 365
        for m in range(1, self.month):
            days += self._days_in_month(m, self.year)
        days += self.day
        return days

    def get_day_name(self):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        total = self._total_days_from_epoch()
        return days[total % 7]

    def get_zeller_congruence_result(self):
        y = self.year
        m = self.month
        if m < 3:
            m += 12
            y -= 1
        k = y % 100
        j = y // 100
        h = (self.day + (13 * (m + 1)) // 5 + k + k // 4 + j // 4 + 5 * j) % 7
        return h

    def is_valid_date(self):
        return self.day <= self._days_in_month(self.month, self.year)

if __name__ == '__main__':
    calc = DateCalculator(2024, 2, 29)
    print(calc.get_day_name())
    print(calc.is_valid_date())
    print(calc.get_zeller_congruence_result())