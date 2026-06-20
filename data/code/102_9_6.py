import datetime

def is_weekday(date_obj):
    return date_obj.weekday() < 5
if __name__ == '__main__':
    sample_dates = [datetime.date(2023, 10, 27), datetime.date(2023, 10, 28), datetime.date(2023, 10, 29), datetime.date(2023, 10, 30)]
    results = {date: is_weekday(date) for date in sample_dates}
    for date, weekday_status in results.items():
        print(f'Is {date} a weekday? {weekday_status}')