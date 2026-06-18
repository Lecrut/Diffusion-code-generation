import datetime
def calculate_days_between(date1: datetime.date, date2: datetime.date) -> int:
    return abs((date2 - date1).days)
if __name__ == '__main__':
    sample_date_1 = datetime.date(2023, 6, 15)
    sample_date_2 = datetime.date(2024, 7, 20)
    days_diff = calculate_days_between(sample_date_1, sample_date_2)
    print(days_diff)