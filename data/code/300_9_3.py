import calendar
def calculate_days_remaining(year: int, month: int) -> int:
    if not 1 <= month <= 12:
        raise ValueError("Month must be between 1 and 12.")
    _, days_in_month = calendar.monthrange(year, month)
    return days_in_month
if __name__ == '__main__':
    sample_year = 2023
    sample_month = 10
    try:
        remaining_days = calculate_days_remaining(sample_year, sample_month)
        print(f"Year: {sample_year}, Month: {sample_month}")
        print(f"Total days in {sample_month}/{sample_year}: {remaining_days}")
    except ValueError as e:
        print(f"Error: {e}")