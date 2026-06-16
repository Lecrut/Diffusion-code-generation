import calendar
def calculate_days_remaining(year: int, month: int) -> int:
    if not 1 <= month <= 12:
        raise ValueError("Month must be between 1 and 12.")
    _, num_days_in_month = calendar.monthrange(year, month)
    return num_days_in_month
if __name__ == '__main__':
    sample_year = 2023
    sample_month = 10
    remaining_days = calculate_days_remaining(sample_year, sample_month)
    print(f"The number of days in {sample_year}-{sample_month:02d} is: {remaining_days}")