class DayOfWeekCalculator:
    DAYS = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    MONTH_DAYS = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    @staticmethod
    def _is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    @staticmethod
    def _adjust_month(year, month):
        if month < 3:
            return month + 12, year - 1
        return month, year

    def calculate(self, year, month, day):
        if not self._is_leap_year(year):
            days_in_current_month = self.MONTH_DAYS[month]
            if day > days_in_current_month:
                raise ValueError("Invalid day for the given month and year")
        adjusted_month, adjusted_year = self._adjust_month(year, month)
        k = adjusted_year % 100
        j = adjusted_year // 100
        h = (day + (13 * (adjusted_month + 1)) // 5 + k + k // 4 + j // 4 + 5 * j) % 7
        return self.DAYS[h]

if __name__ == '__main__':
    calculator = DayOfWeekCalculator()
    result = calculator.calculate(2024, 2, 29)
    print(result)