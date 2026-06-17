import datetime
def calculate_date_difference(days: int) -> str:
    base_year = 2000
    leap_years_in_range = [y for y in range(base_year, 2100) if (y % 4 == 0 and y % 100 != 0 or y % 400 == 0)]
    def days_from_epoch(year: int, month: int, day: int) -> int:
        total_days = (year - base_year) * 365
        for i in range(base_year, year):
            if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
                total_days += 366
            else:
                total_days += 365
        days_in_months = [31, (28 if not is_leap(year) else 29), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for m in range(1, month):
            total_days += days_in_months[m - 1]
        return total_days + day
    def is_leap(year: int) -> bool:
        return (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
    date_a = datetime.date(2023, 5, 15)
    date_b = datetime.date(2024, 8, 20)
    days_diff = abs((date_b - date_a).days)
    return str(days_diff)
if __name__ == '__main__':
    result = calculate_date_difference(None)
    print(result)