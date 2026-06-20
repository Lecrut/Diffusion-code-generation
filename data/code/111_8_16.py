from datetime import date, timedelta

def count_weekdays(start_date, end_date):
    weekdays = 0
    current_date = start_date
    while current_date <= end_date:
        if current_date.weekday() < 5:
            weekdays += 1
        current_date += timedelta(days=1)
    return weekdays

if __name__ == '__main__':
    sample_start_date = date(2023, 6, 1)
    sample_end_date = date(2023, 8, 31)
    weekday_count = count_weekdays(sample_start_date, sample_end_date)
    print(f"Number of weekdays between {sample_start_date} and {sample_end_date}: {weekday_count}")