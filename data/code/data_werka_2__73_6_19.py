import datetime

def calculate_date_difference(start_date: datetime.date, end_date: datetime.date) -> int:
    delta = end_date - start_date
    return delta.days

if __name__ == '__main__':
    start = datetime.date(2023, 1, 1)
    end = datetime.date(2023, 12, 31)
    result = calculate_date_difference(start, end)
    print(result)