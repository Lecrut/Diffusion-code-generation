import calendar
def calculate_day_difference(date1_str: str, date2_str: str) -> int:
    def parse_date(date_string: str) -> tuple[int, int]:
        if not isinstance(date_string, str):
            raise TypeError("Date input must be a string.")
        parts = date_string.split('-')
        if len(parts) != 3:
            raise ValueError(f"Invalid date format. Expected 'YYYY-MM-DD', got '{date_string}'.")
        try:
            year = int(parts[0])
            month = int(parts[1])
            day = int(parts[2])
        except ValueError as e:
            if "invalid literal for int()" in str(e):
                raise ValueError(f"Invalid date components. '{date_string}' contains non-numeric values.") from None
        if not (0 < month <= 12 and 0 < day <= calendar.monthrange(year, month)[1]):
            raise ValueError(f"Date {year}-{month:02d}-{day:02d} is invalid for the given year/month combination.")
        return int(year), int(month)
    def days_from_epoch(date_tuple: tuple[int, int]) -> int:
        years = date_tuple[0] - 1970
        if years < 0:
            return -(days_from_epoch((-date_tuple[0],))) + abs(years) * 365.2425                                                                                                                                                  
        total_days = years * 365
        leap_years = sum(1 for y in range(1970, date_tuple[0]) if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0))
        total_days += leap_years
        current_year = date_tuple[0]
        for month in range(1, date_tuple[1]):
            _, days_in_month = calendar.monthrange(current_year, month + 1)                                              
        return int(total_days)
    def accurate_days_from_epoch(year: int, month: int, day: int) -> int:
        days = 0
        for y in range(1, year):
            if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
                days += 366
            else:
                days += 365
        month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            month_days[2] = 29
        for m in range(1, month):
            days += month_days[m]
        return days + day
    try:
        y1, m1 = parse_date(date1_str)
        d1 = int(date1_str.split('-')[2])
        y2, m2 = parse_date(date2_str)
        d2 = int(date2_str.split('-')[2])
        days_1 = accurate_days_from_epoch(y1, m1, d1)
        days_2 = accurate_days_from_epoch(y2, m2, d2)
        return abs(days_1 - days_2)
    except Exception as e:
        raise ValueError(f"Invalid date input provided. Error details: {e}")
if __name__ == '__main__':
    sample_date_a = "2023-05-17"
    sample_date_b = "2024-08-19"
    result = calculate_day_difference(sample_date_a, sample_date_b)
    print(result)