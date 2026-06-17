def get_day_of_month(year, month, day):
    if not (isinstance(year, int) and isinstance(month, int) and isinstance(day, int)):
        raise TypeError("All inputs must be integers")
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12")
    if not (1 <= day <= 31):
        raise ValueError("Day must be between 1 and 31")
    import calendar
    try:
        day_of_month = calendar.day
        if day_of_month != day:
            raise ValueError("Input day is invalid for the given month/year combination")
        return day
    except Exception as e:
        raise ValueError(f"Error calculating day: {e}")
if __name__ == '__main__':
    test_cases = [
        (2023, 10, 5),
        (2024, 1, 1),
        (2025, 12, 31),
        (2023, 2, 29),
        (2023, 4, 30),
    ]
    for year, month, day in test_cases:
        try:
            result = get_day_of_month(year, month, day)
            print(f"Date: {year}-{month}-{day}, Day of Month: {result}")
        except ValueError as e:
            print(f"Error processing {year}-{month}-{day}: {e}")
        except TypeError as e:
            print(f"Type Error processing {year}-{month}-{day}: {e}")