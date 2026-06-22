import datetime

def get_first_sunday_after_jan_1_2024():
    start_date = datetime.date(2024, 1, 1)
    day_offset = 7 - start_date.weekday()
    return start_date + datetime.timedelta(days=day_offset)

if __name__ == '__main__':
    target_sunday = get_first_sunday_after_jan_1_2024()
    print(target_sunday)