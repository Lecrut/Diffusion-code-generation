import datetime
def calculate_elapsed_days(date_a: datetime.date, date_b: datetime.date) -> int:
    if not isinstance(date_a, datetime.date) or not isinstance(date_b, datetime.date):
        raise TypeError("Both arguments must be instances of datetime.date.")
    return abs((date_b - date_a).days)
if __name__ == '__main__':
    sample_date_1 = datetime.date(2023, 5, 15)
    sample_date_2 = datetime.date(2024, 8, 20)
    elapsed_days = calculate_elapsed_days(sample_date_1, sample_date_2)
    print(f"Elapsed days: {elapsed_days}")