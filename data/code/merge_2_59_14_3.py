import datetime
def get_day_of_week(date: datetime.date) -> str:
    return date.strftime("%A")
if __name__ == '__main__':
    sample_dates = [
        datetime.date(2023, 10, 5),
        datetime.date(2024, 6, 17),
        datetime.datetime.now().date(),
    ]
    for d in sample_dates:
        print(f"{d}: {get_day_of_week(d)}")