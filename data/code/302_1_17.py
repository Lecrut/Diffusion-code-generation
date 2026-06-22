FEBRUARY = 2
LEAP_YEAR_THRESHOLD_100 = 100
LEAP_YEAR_THRESHOLD_400 = 400

def days_in_month(year, month):
    if month == FEBRUARY:
        return 29 if year % 4 == 0 and year % LEAP_YEAR_THRESHOLD_100 != 0 or year % LEAP_YEAR_THRESHOLD_400 == 0 else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31
if __name__ == '__main__':
    print(days_in_month(2020, FEBRUARY))
    print(days_in_month(2019, FEBRUARY))
    print(days_in_month(2021, 4))