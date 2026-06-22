DAYS_PER_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
LEAP_YEAR_THRESHOLD_4 = 4
LEAP_YEAR_THRESHOLD_100 = 100
LEAP_YEAR_THRESHOLD_400 = 400

def is_leap_year(year):
    return year % LEAP_YEAR_THRESHOLD_4 == 0 and (year % LEAP_YEAR_THRESHOLD_100 != 0 or year % LEAP_YEAR_THRESHOLD_400 == 0)

def days_in_month(year, month):
    if not 1 <= year <= 9999 or not 1 <= month <= 12:
        raise ValueError('Year must be between 1 and 9999, and month must be between 1 and 12')
    
    days = DAYS_PER_MONTH[month - 1]
    if month == 2 and is_leap_year(year):
        days += 1
    
    return days

if __name__ == '__main__':
    print(days_in_month(2023, 2))
    print(days_in_month(2024, 2))
    print(days_in_month(2023, 4))