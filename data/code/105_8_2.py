import datetime
def calculate_future_date(start_date):
    if start_date is None:
        return None
    try:
        start = datetime.date(start_date.year, start_date.month, start_date.day)
        future_date = start + datetime.timedelta(days=366)
        return future_date
    except ValueError:
        return None
if __name__ == '__main__':
    sample_date_str = "2023-10-26"
    try:
        start_date = datetime.date.fromisoformat(sample_date_str)
        result_date = calculate_future_date(start_date)
        print(result_date.isoformat())
    except ValueError:
        print("Invalid date format provided.")