import datetime

def calculate_year_difference(start_date: datetime.datetime, end_date: datetime.datetime) -> int:
    if not isinstance(start_date, datetime.datetime) or not isinstance(end_date, datetime.datetime):
        raise ValueError('Both inputs must be datetime objects')
    year_diff = end_date.year - start_date.year
    if (end_date.month, end_date.day) < (start_date.month, start_date.day):
        year_diff -= 1
    return year_diff
if __name__ == '__main__':
    start = datetime.datetime(2020, 5, 15, 10, 30, 0)
    end = datetime.datetime(2023, 5, 14, 10, 30, 0)
    result = calculate_year_difference(start, end)
    print(result)
    start2 = datetime.datetime(2020, 5, 15, 10, 30, 0)
    end2 = datetime.datetime(2023, 5, 15, 10, 30, 0)
    result2 = calculate_year_difference(start2, end2)
    print(result2)
    start3 = datetime.datetime(2020, 1, 1, 0, 0, 0)
    end3 = datetime.datetime(2020, 12, 31, 23, 59, 59)
    result3 = calculate_year_difference(start3, end3)
    print(result3)