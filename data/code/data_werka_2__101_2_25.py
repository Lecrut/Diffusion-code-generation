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
            m += 12
            y -= 1

        k = y % 100
        j = y // 100

        h = (d + (13 * (m + 1)) // 5 + k + k // 4 + j // 4 + 5 * j) % 7

        days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        return days[h]

    def get_date_string(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d}"

if __name__ == '__main__':
    calc = DayOfWeekCalculator(2024, 2, 29)
    day_name = calc.calculate()
    date_str = calc.get_date_string()
    print(f"Date: {date_str}, Day: {day_name}")
    
    calc2 = DayOfWeekCalculator(2023, 1, 1)
    print(f"Date: {calc2.get_date_string()}, Day: {calc2.calculate()}")