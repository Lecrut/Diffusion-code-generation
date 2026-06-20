import datetime

def get_day_of_month(date: datetime.date) -> int:
    return date.day

if __name__ == '__main__':
    sample_date = datetime.date(2023, 11, 4)
    day_of_month = get_day_of_month(sample_date)
    print(day_of_month)