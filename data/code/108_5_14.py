import datetime

DAY_OF_MONTH = "day"

def get_day_of_month(date: datetime.datetime) -> int:
    return getattr(date, DAY_OF_MONTH)

if __name__ == '__main__':
    sample_date = datetime.datetime(2023, 9, 15)
    print(get_day_of_month(sample_date))