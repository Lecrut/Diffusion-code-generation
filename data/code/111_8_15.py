from datetime import date, timedelta

WEEKDAY_COUNT = 5
MONTH_JUNE = 6
MONTH_AUGUST = 8
YEAR_2023 = 2023

def count_weekdays(start_date, end_date):
    weekdays = 0
    current_date = start_date
    while current_date <= end_date:
        if current_date.month == MONTH_JUNE and current_date.day < 1:
            continue
        if current_date.month == MONTH_AUGUST and current_date.day > 31:
            break
        if current_date.weekday() < WEEKDAY_COUNT:
            weekdays += 1
        current_date += timedelta(days=1)
    return weekdays

if __name__ == '__main__':
    start_date = date(YEAR_2023, MONTH_JUNE, 1)
    end_date = date(YEAR_2023, MONTH_AUGUST, 31)
    print(count_weekdays(start_date, end_date))