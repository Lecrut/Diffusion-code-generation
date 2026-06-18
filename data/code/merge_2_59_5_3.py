import datetime
def calculate_weekday(date: datetime.date) -> int:
    return date.weekday()
if __name__ == '__main__':
    sample_date = datetime.datetime(2023, 10, 5).date()
    result = calculate_weekday(sample_date)
    print(result)