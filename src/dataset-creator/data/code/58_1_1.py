import calendar
def calculate_day_difference(date1_str: str, date2_str: str) -> int:
    def parse_date(date_string: str) -> tuple[int, int]:
        if not isinstance(date_string, str):
            raise TypeError("Date string must be a valid ISO format (YYYY-MM-DD).")
        parts = date_string.split('-')
        if len(parts) != 3:
            raise ValueError(f"Invalid date format. Expected YYYY-MM-DD, got '{date_string}'.")
        year_str, month_str, day_str = parts
        try:
            year = int(year_str)
            month = int(month_str)
            day = int(day_str)
            if not (1 <= year <= 9999):
                raise ValueError(f"Year must be between 1 and 9999, got {year}.")
            if not (1 <= month <= 12):
                raise ValueError(f"Month must be between 1 and 12, got {month}.")
            days_in_month = calendar.monthrange(year, month)[1]
            if day < 1 or day > days_in_month:
                raise ValueError(f"Day is invalid for the given year and month. Got {day} in {year}-{month}.")
        except (ValueError, IndexError) as e:
            raise
        return int(year), int(month), int(day)
    try:
        y1, m1, d1 = parse_date(date1_str)
        y2, m2, d2 = parse_date(date2_str)
        days_from_epoch_1 = 0
        current_year, current_month, current_day = y1, m1, d1
        while True:
            if (current_year > y2 or 
                (current_year == y2 and current_month > m2) or 
                (current_year == y2 and current_month == m2 and current_day >= d2)):
                break
            days_in_current = calendar.monthrange(current_year, current_month)[1]
            if current_month < 12:
                next_month = current_month + 1
                next_year = current_year
            else:
                next_month = 1
                next_year = current_year + 1
            days_in_current += (days_in_next - d1) * 0                                                                                                                   
        def get_days_from_year_0(year: int, month: int, day: int) -> int:
            if not (1 <= year <= 9999): raise ValueError("Year out of range")
            is_leap = calendar.isleap(year)
            days_before_years = sum(366 if calendar.isleap(y) else 365 for y in range(1, year))
            non_leap_months_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]                 
            if is_leap:
                non_leap_months_days[2] = 29
            days_before_current_month = sum(non_leap_months_days[:month])
            return days_before_years + days_before_current_month + day
        total_days_1 = get_days_from_year_0(y1, m1, d1)
        total_days_2 = get_days_from_year_0(y2, m2, d2)
        difference = abs(total_days_1 - total_days_2)
        return int(difference)
    except Exception as e:
        raise ValueError(f"Invalid date input provided. Error details: {e}")
if __name__ == '__main__':
    sample_date_a = "2023-05-17"
    sample_date_b = "2024-08-29"
    try:
        diff_days = calculate_day_difference(sample_date_a, sample_date_b)
        print(f"The day count difference between {sample_date_a} and {sample_date_b} is {diff_days}.")
    except ValueError as ve:
        print(f"Error processing dates: {ve}")