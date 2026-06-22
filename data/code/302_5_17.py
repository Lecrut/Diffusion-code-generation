def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
days_in_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

def calculate_total_days(year):
    total_days = 0
    for month in range(1, 13):
        if month == 2:
            total_days += days_in_month[month] + int(is_leap_year(year))
        else:
            total_days += days_in_month[month]
    return total_days
if __name__ == '__main__':
    print(calculate_total_days(2023))
    print(calculate_total_days(2024))