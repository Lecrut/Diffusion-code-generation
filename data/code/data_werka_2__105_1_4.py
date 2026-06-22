import datetime

def get_first_sunday_after_jan_1_2024():
    base_date = datetime.date(2024, 1, 1)
    days_ahead = 6 - base_date.weekday()
    if days_ahead == 0:
        target_date = base_date + datetime.timedelta(days=7)
    else:
        target_date = base_date + datetime.timedelta(days=days_ahead)
    return target_date

if __name__ == '__main__':
    sample_date = datetime.date(2024, 1, 1)
    computed_sunday = get_first_sunday_after_jan_1_2024()
    print(computed_sunday)