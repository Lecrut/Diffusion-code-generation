def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_days_in_month(year, month):
    if month not in range(1, 13):
        raise ValueError("Month must be between 1 and 12")
    
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2:
        return 29 if is_leap_year(year) else 28
    return days_in_month[month]

if __name__ == '__main__':
    year1 = 2023
    month1 = 10
    day1 = get_days_in_month(year1, month1)
    print(f"Day of the month for {year1}-{month1:02d}: {day1}")