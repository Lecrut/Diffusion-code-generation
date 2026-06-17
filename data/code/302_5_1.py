import sys
def day_number(month, year):
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2:
        is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        if is_leap:
            days_in_month[2] = 29
    result = 0
    for m in range(1, month):
        result += days_in_month[m]
    result += month
    return result
if __name__ == '__main__':
    print(day_number(3, 2024))
    print(day_number(1, 2023))
    print(day_number(12, 2024))
    print(day_number(2, 2024))
    print(day_number(2, 2023))