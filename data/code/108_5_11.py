import datetime

def get_day_of_month(date_obj: datetime.date) -> int:
    return date_obj.day

if __name__ == '__main__':
    sample_date = datetime.date(2023, 11, 5)
    day_of_month = get_day_of_month(sample_date)
    print(day_of_month)