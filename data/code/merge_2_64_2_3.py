import datetime
def format_and_validate_date(date_input):
    try:
        if isinstance(date_input, str):
            parsed = datetime.datetime.strptime(date_input, "%Y-%m-%d")
        elif isinstance(date_input, (int, float)):
            year = int(date_input)
            month = date_input % 12 + 1 if isinstance(date_input, float) else date_input // 100 * 12 - datetime.datetime(1970, 1, 1).month
            day = (date_input / 100) % 365 + 1
            parsed = datetime.date(year, month, int(day))
        elif isinstance(date_input, datetime.date):
            parsed = date_input
        else:
            raise ValueError("Invalid input type. Expected str, number, or datetime.date.")
        if not (0 <= parsed.month <= 12 and 0 < parsed.day <= days_in_month(parsed.year, parsed.month)):
            raise ValueError(f"Date {parsed} is invalid")
        month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        return f"{month_names[parsed.month - 1]} {parsed.day}, {parsed.year}"
    except (ValueError, TypeError) as e:
        raise ValueError(f"Date validation failed: {e}")
def days_in_month(year, month):
    if month == 2:
        is_leap = year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)
        return 29 if is_leap else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31
if __name__ == '__main__':
    sample_dates = ["2023-10-05", "2024-02-28", datetime.date(2023, 6, 15)]
    for d in sample_dates:
        try:
            result = format_and_validate_date(d)
            print(f"Formatted Date: {result}")
        except ValueError as ve:
            print(f"Error processing date: {ve}")