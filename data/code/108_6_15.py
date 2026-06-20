import calendar

def validate_date(date):
    if not isinstance(date, tuple) or len(date) != 3:
        return False, "Date must be a tuple of (year, month, day)"
    year, month, day = date
    if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
        return False, "All inputs must be integers."
    if not (1 <= month <= 12):
        return False, "Month must be between 1 and 12."
    if not (1 <= day <= calendar.monthrange(year, month)[1]):
        return False, f"Day must be between 1 and {calendar.monthrange(year, month)[1]}"
    return True, date

def get_day_of_month(date):
    is_valid, validated_date = validate_date(date)
    if not is_valid:
        raise ValueError(validated_date)
    year, month, day = validated_date
    return calendar.monthrange(year, month)[1] - day + 1

if __name__ == '__main__':
    sample_dates = [(2023, 10, 5), (2024, 2, 29), (2021, 12, 31)]
    for date in sample_dates:
        print(f"The day of the month for {date} is: {get_day_of_month(date)}")