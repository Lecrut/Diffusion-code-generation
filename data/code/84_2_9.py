from math import floor
EPOCH_YEAR = 1753
MONTH_DAYS = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def day_of_year(year, month, day):
    leap_days = floor((year - EPOCH_YEAR) / 4) - floor((year - EPOCH_YEAR) / 100) + floor((year - EPOCH_YEAR) / 400)
    total_days = (year - EPOCH_YEAR) * 365 + leap_days
    month_offset = sum(MONTH_DAYS[:month])
    if is_leap_year(year) and month > 2:
        month_offset += 1
    return total_days + month_offset + day
if __name__ == '__main__':
    print(day_of_year(2023, 10, 27))