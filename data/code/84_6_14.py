import calendar

def get_day_number(year: int, month: int, day: int) -> int:
    if year < 1:
        raise ValueError("Year must be a positive integer")
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12")
    if not (1 <= day <= calendar.monthrange(year, month)[1]):
        raise ValueError("Day must be valid for the given month and year")

    return calendar.timegm((year, month, day, 0, 0, 0)) // (60 * 60 * 24) + 1

if __name__ == '__main__':
    print(get_day_number(2023, 1, 1))
    print(get_day_number(2024, 2, 29))
    print(get_day_number(2024, 3, 1))