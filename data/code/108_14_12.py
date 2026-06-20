def is_leap_year(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_days_in_month(year: int, month: int) -> int:
    days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leap_year(year):
        return 29
    return days_per_month[month - 1]

def get_day_of_month(date_string: str) -> int:
    try:
        year, month, day = map(int, date_string.split('-'))
        if month < 1 or month > 12:
            raise ValueError("Month must be between 1 and 12.")
        if day < 1 or day > get_days_in_month(year, month):
            raise ValueError("Day is out of range for the given month and year.")
        return day
    except (ValueError, TypeError) as e:
        raise ValueError(f"Invalid date format. Please use YYYY-MM-DD: {e}")

if __name__ == '__main__':
    sample_date_1 = "2023-10-27"
    sample_date_2 = "1999-01-01"
    sample_date_3 = "2024-02-29"
    print(f"Day of month for {sample_date_1}: {get_day_of_month(sample_date_1)}")
    print(f"Day of month for {sample_date_2}: {get_day_of_month(sample_date_2)}")
    print(f"Day of month for {sample_date_3}: {get_day_of_month(sample_date_3)}")