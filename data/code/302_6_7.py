class MonthDays:
    MONTHS_WITH_31_DAYS = {1, 3, 5, 7, 8, 10, 12}
    FEBRUARY = 2

    @staticmethod
    def is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    @staticmethod
    def get_days_in_month(year, month):
        if month in MonthDays.MONTHS_WITH_31_DAYS:
            return 31
        elif month == MonthDays.FEBRUARY:
            return 29 if MonthDays.is_leap_year(year) else 28
        else:
            return 30

if __name__ == '__main__':
    year1 = 2023
    month1 = 1
    result1 = MonthDays.get_days_in_month(year1, month1)
    print(f"Year: {year1}, Month: {month1}, Days in month: {result1}")
    
    year2 = 2024
    month2 = 2
    result2 = MonthDays.get_days_in_month(year2, month2)
    print(f"Year: {year2}, Month: {month2}, Days in month: {result2}")
    
    year3 = 2023
    month3 = 12
    result3 = MonthDays.get_days_in_month(year3, month3)
    print(f"Year: {year3}, Month: {month3}, Days in month: {result3}")