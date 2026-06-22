class DayOfWeekCalculator:
    MONTH_ADJUSTMENT = 1
    YEAR_OFFSET = 1
    CENTURY_MULTIPLIER = 13
    FIVE_DIVISOR = 5
    HUNDRED_BASE = 100

    @staticmethod
    def adjust_month_and_year(month, year):
        if month < 3:
            return month + DayOfWeekCalculator.MONTH_ADJUSTMENT, year - DayOfWeekCalculator.YEAR_OFFSET
        return month, year

    @staticmethod
    def get_day_of_week(year, month, day):
        adjusted_month, adjusted_year = DayOfWeekCalculator.adjust_month_and_year(month, year)
        k = adjusted_year % DayOfWeekCalculator.HUNDRED_BASE
        j = adjusted_year // DayOfWeekCalculator.HUNDRED_BASE
        h = (day + (DayOfWeekCalculator.CENTURY_MULTIPLIER * (adjusted_month + DayOfWeekCalculator.MONTH_ADJUSTMENT)) // DayOfWeekCalculator.FIVE_DIVISOR + k + k // 4 + j // 4 - 2 * j) % 7
        return h

if __name__ == '__main__':
    result = DayOfWeekCalculator.get_day_of_week(1900, 1, 1)
    print(result)