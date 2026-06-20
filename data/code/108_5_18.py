import datetime

def get_day_of_month(date: datetime.datetime) -> int:
    return date.day

if __name__ == '__main__':
    sample_date = datetime.datetime(2023, 11, 4)
    day_of_month = get_day_of_month(sample_date)
    print(day_of_month)