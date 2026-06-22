def days_in_month(year: int, month: int) -> int:
    if not 1 <= month <= 12:
        raise ValueError('Month must be between 1 and 12.')
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        if month == 2:
            return 29
        elif month in [4, 6, 9, 11]:
            return 30
        else:
            return 31
    elif month == 2:
        return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31
if __name__ == '__main__':
    print(days_in_month(2023, 10))
    print(days_in_month(2024, 2))