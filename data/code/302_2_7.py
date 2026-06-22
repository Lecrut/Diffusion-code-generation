def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(year, month):
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12")
    
    if month == 2:
        return 29 if is_leap_year(year) else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

if __name__ == '__main__':
    year1 = 2023
    month1 = 10
    day1 = days_in_month(year1, month1)
    print(f"Day of the month for {year1}-{month1:02d}: {day1}")
    
    year2 = 2024
    month2 = 2
    day2 = days_in_month(year2, month2)
    print(f"Day of the month for {year2}-{month2:02d}: {day2}")