import datetime

def first_sunday_after_jan_1_2024():
    start_date = datetime.date(2024, 1, 1)
    days_ahead = 6 - start_date.weekday()
    if days_ahead == 0:
        days_ahead = 7
    target_date = start_date + datetime.timedelta(days=days_ahead)
    return target_date

if __name__ == '__main__':
    result = first_sunday_after_jan_1_2024()
    print(result)