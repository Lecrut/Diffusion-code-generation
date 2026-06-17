def day_number(year, month):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    if month == 2 and is_leap:
        return day_number(year, 2, days_in_month) + 1
    if month == 2 and not is_leap:
        return day_number(year, 2, days_in_month)
    return sum(days_in_month[:month]) + month
def day_number(year, month):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    if month > 2:
        base = sum(days_in_month[:2]) + (31 if month == 3 else 30) + (31 if month == 4 else 30) + (31 if month == 5 else 30) + (31 if month == 6 else 30) + (31 if month == 7 else 31) + (31 if month == 8 else 31) + (30 if month == 9 else 30) + (31 if month == 10 else 31) + (30 if month == 11 else 30) + (31 if month == 12 else 31)
        return base + (month - 2)
    days = [31, 28] if month == 2 else [31]
    if is_leap:
        days[1] = 29
    return sum(days[:month]) + month
if __name__ == '__main__':
    print(day_number(2024, 3))
    print(day_number(2024, 2))
    print(day_number(2023, 2))
    print(day_number(2000, 2))