import datetime

def get_day_of_month(date_obj: datetime.date) -> int:
    return date_obj.day

if __name__ == '__main__':
    sample_date = datetime.date(2023, 10, 15)
    result = get_day_of_month(sample_date)
    print(result)