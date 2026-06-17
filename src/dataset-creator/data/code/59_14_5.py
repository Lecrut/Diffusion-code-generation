import datetime
def date_to_day_of_week(date: datetime.date) -> str:
    return date.strftime("%A")
if __name__ == '__main__':
    sample_dates = [
        datetime.datetime(2023, 10, 5).date(),
        datetime.datetime.now().date(),
        datetime.date.today() + datetime.timedelta(days=7),
    ]
    for date in sample_dates:
        print(f"Date: {date} -> Day of Week: {date_to_day_of_week(date)}")