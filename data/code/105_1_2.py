from datetime import date, timedelta

def first_sunday_after_jan_1():
    target_date = date(2024, 1, 1)
    while target_date.weekday() != 6:
        target_date += timedelta(days=1)
    return target_date

if __name__ == '__main__':
    print(first_sunday_after_jan_1())