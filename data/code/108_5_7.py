import datetime

def get_day_of_month(date: datetime.datetime) -> int:
    return date.day

if __name__ == '__main__':
    sample_date = datetime.datetime(2023, 9, 15)
    print(get_day_of_month(sample_date))