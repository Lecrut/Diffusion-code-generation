import datetime

def is_leap_year(year: int) -> bool:
    """Check if a year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(year: int, month: int) -> int:
    """Return the number of days in a given month of a specific year."""
    if month == 2:
        return 29 if is_leap_year(year) else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def calculate_duration_days(date1_str: str, date2_str: str) -> int:
    """
    Calculate the number of days between two dates provided as strings in 'YYYY-MM-DD' format.
    
    Args:
        date1_str (str): First date string in 'YYYY-MM-DD' format.
        date2_str (str): Second date string in 'YYYY-MM-DD' format.
        
    Returns:
        int: The absolute number of days between the two dates.
    """
    def parse_date(date_string: str) -> datetime.date:
        year, month, day = map(int, date_string.split('-'))
        return datetime.date(year, month, day)

    d1 = parse_date(date1_str)
    d2 = parse_date(date2_str)

    delta = d2 - d1
    return abs(delta.days)

if __name__ == '__main__':
    # Sample values hard-coded to ensure no user input or external dependencies are needed.
    sample_date_1 = "2023-06-15"
    sample_date_2 = "2024-06-15"

    duration_days = calculate_duration_days(sample_date_1, sample_date_2)

    print(f"The number of days between {sample_date_1} and {sample_date_2} is: {duration_days}")