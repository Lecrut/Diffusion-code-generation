import time
DAYS_IN_MONTH = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def get_day_of_month():
    current_time = time.localtime()
    year = current_time.tm_year
    month = current_time.tm_mon
    day = current_time.tm_mday
    if not 1 <= day <= DAYS_IN_MONTH[month]:
        raise ValueError(f'Invalid day for month {month} in {year}: {day}')
    return day
if __name__ == '__main__':
    print(get_day_of_month())