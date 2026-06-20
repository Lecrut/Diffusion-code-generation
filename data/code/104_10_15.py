import datetime

def compare_dates(date1: datetime.date, date2: datetime.date) -> int:
    if not isinstance(date1, datetime.date) or not isinstance(date2, datetime.date):
        raise ValueError('Both inputs must be instances of datetime.date')
    return (date1 - date2).days
if __name__ == '__main__':
    sample_date1 = datetime.date(2023, 10, 5)
    sample_date2 = datetime.date(2023, 9, 15)
    print(compare_dates(sample_date1, sample_date2))