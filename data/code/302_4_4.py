import calendar
def get_day_of_month(year, month, day):
    if not (isinstance(year, int) and isinstance(month, int) and isinstance(day, int)):
        raise TypeError("All inputs must be integers.")
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12.")
    if not (1 <= day <= calendar.monthrange(year, month)[1]):
        raise ValueError(f"Day {day} is invalid for month {month} in year {year}.")
    return day
if __name__ == '__main__':
    test_date_1 = (2023, 10, 15)
    test_date_2 = (2024, 1, 1)
    test_date_3 = (2023, 12, 31)
    test_date_4 = (2025, 2, 5)
    invalid_date_month = (2023, 13, 1)
    invalid_date_day = (2023, 10, 32)
    print(f"Day of month for {test_date_1}: {get_day_of_month(*test_date_1)}")
    print(f"Day of month for {test_date_2}: {get_day_of_month(*test_date_2)}")
    print(f"Day of month for {test_date_3}: {get_day_of_month(*test_date_3)}")
    print(f"Day of month for {test_date_4}: {get_day_of_month(*test_date_4)}")
    try:
        get_day_of_month(*invalid_date_month)
    except ValueError as e:
        print(f"Error caught for invalid month input: {e}")
    try:
        get_day_of_month(*invalid_date_day)
    except ValueError as e:
        print(f"Error caught for invalid day input: {e}")