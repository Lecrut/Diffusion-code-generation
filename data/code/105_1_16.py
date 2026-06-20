import datetime

def find_first_sunday_after_jan_1():
    target_date = datetime.date(2024, 1, 1)
    while target_date.weekday() != 6:
        target_date += datetime.timedelta(days=1)
    return target_date

if __name__ == '__main__':
    sample_date = datetime.date(2024, 3, 15)
    result = find_first_sunday_after_jan_1()
    print(f"First Sunday after January 1, 2024: {result}")