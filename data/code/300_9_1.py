import calendar
def calculate_days_remaining(year: int, month: int) -> int:
    if not 1 <= month <= 12 or not 1 <= year <= 9999:
        raise ValueError("Invalid year or month provided.")
    _, days_in_month = calendar.monthrange(year, month)
    return days_in_month
if __name__ == '__main__':
    sample_year = 2023
    sample_month = 10
    try:
        days = calculate_days_remaining(sample_year, sample_month)
        print(f"The number of days in {sample_year}-{sample_month:02d} is: {days}")
    except ValueError as e:
        print(f"Error: {e}")