FEBRUARY_DAYS = 28
LEAP_YEAR_FEBRUARY_DAYS = 29

def days_in_month(year):
    months_days = {
        1: 31, 
        2: FEBRUARY_DAYS, 
        3: 31, 
        4: 30, 
        5: 31, 
        6: 30, 
        7: 31, 
        8: 31, 
        9: 30, 
        10: 31, 
        11: 30, 
        12: 31
    }
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        months_days[2] = LEAP_YEAR_FEBRUARY_DAYS
    return months_days

if __name__ == '__main__':
    print(days_in_month(2024))
    print(days_in_month(2023))