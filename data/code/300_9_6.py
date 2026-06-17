import calendar
def calculate_days_remaining(year: int, month: int) -> int:
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12.")
    _, num_days_in_month = calendar.monthrange(year, month)
    return num_days_in_month
if __name__ == '__main__':
    year = 2023
    month = 10
    try:
        days_remaining = calculate_days_remaining(year, month)
        print(f"Year: {year}, Month: {month}")
        print(f"Days remaining in the month: {days_remaining}")
    except ValueError as e:
        print(f"Error: {e}")