import time

def is_weekday():
    current_time = time.localtime()
    day_of_week = current_time.tm_wday
    return day_of_week < 5

if __name__ == '__main__':
    sample_date = (2023, 10, 25)
    date_object = time.struct_time((sample_date[0], sample_date[1], sample_date[2], 0, 0, 0, sample_date[2], 274, -1))
    weekday_check = is_weekday(date_object)
    print(weekday_check)