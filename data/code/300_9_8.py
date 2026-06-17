import calendar
def calculate_days_remaining(year: int, month: int, day: int) -> int:
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12.")
    if not (1 <= day <= calendar.monthrange(year, month)[1]):
        raise ValueError(f"Day {day} is invalid for month {month} in year {year}.")
    _, num_days = calendar.monthrange(year, month)
    remaining_days = num_days - day
    return remaining_days
if __name__ == '__main__':
    sample_year = 2023
    sample_month = 10
    sample_day = 15
    try:
        result = calculate_days_remaining(sample_year, sample_month, sample_day)
        print(f"Year: {sample_year}, Month: {sample_month}, Day: {sample_day}")
        print(f"Days remaining in the month starting from this day: {result}")
        result_start = calculate_days_remaining(2023, 1, 1)
        print(f"\nDays remaining in January 2023 starting from Jan 1st: {result_start}")
    except ValueError as e:
        print(f"Error: {e}")