from datetime import date, timedelta, datetime
def get_next_upcoming_date(input_date: date) -> datetime:
    next_date = input_date + timedelta(days=1)
    return datetime.combine(next_date, datetime.min.time())
if __name__ == '__main__':
    sample_date = date(2023, 10, 26)
    result = get_next_upcoming_date(sample_date)
    print(result)