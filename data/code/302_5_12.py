def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(month, year):
    months = {
        1: 31, 2: 28 if not is_leap_year(year) else 29,
        3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    return months[month]

def total_days_in_year(year):
    days = 0
    for month in range(1, 13):
        days += days_in_month(month, year)
    return days

if __name__ == '__main__':
    print(total_days_in_year(2023))
    print(total_days_in_year(2024))