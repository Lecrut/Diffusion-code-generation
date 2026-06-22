from datetime import date, timedelta

def first_sunday_after_jan_1_2024():
    start_date = date(2024, 1, 1)
    current_date = start_date
    while current_date.weekday() != 6:
        current_date += timedelta(days=1)
    return current_date

if __name__ == '__main__':
    result = first_sunday_after_jan_1_2024()
    print(result)