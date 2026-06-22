LEAP_YEAR_THRESHOLD = 400
NON_LEAP_YEAR_THRESHOLD = 100

def is_leap_year(year):
    return (year % LEAP_YEAR_THRESHOLD == 0) or (year % NON_LEAP_YEAR_THRESHOLD != 0 and year % 4 == 0)

def days_in_month(year, month):
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12")
    
    days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if month == 2 and is_leap_year(year):
        return days_per_month[month] + 1
    else:
        return days_per_month[month]

if __name__ == '__main__':
    year1 = 2023
    month1 = 10
    day1 = days_in_month(year1, month1)
    print(f"Day of the month for {year1}-{month1:02d}: {day1}")