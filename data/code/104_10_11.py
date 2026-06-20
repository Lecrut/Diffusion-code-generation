import datetime

def compare_dates(date1: datetime.date, date2: datetime.date) -> int:
    if date1 > date2:
        return 1
    elif date1 < date2:
        return -1
    else:
        return 0
if __name__ == '__main__':
    sample_date1 = datetime.date(2023, 4, 15)
    sample_date2 = datetime.date(2023, 4, 10)
    result = compare_dates(sample_date1, sample_date2)
    print(result)