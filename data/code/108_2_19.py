import time
DAYS_IN_MONTH = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def get_day_of_month():
    current_time = time.localtime()
    year = current_time.tm_year
    month = current_time.tm_mon
    day = current_time.tm_mday
    is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
    if month == 2 and is_leap:
        day += 1
    return day
if __name__ == '__main__':
    print(get_day_of_month())