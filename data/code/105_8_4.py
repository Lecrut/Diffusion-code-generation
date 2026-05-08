import datetime
def calculate_future_date(start_date):
    if not isinstance(start_date, datetime.date):
        raise TypeError("Input must be a datetime.date object")
    future_date = start_date + datetime.timedelta(days=366)
    return future_date
if __name__ == '__main__':
    sample_date_str = "2023-10-26"
    start_date = datetime.datetime.strptime(sample_date_str, "%Y-%m-%d").date()
    future_date = calculate_future_date(start_date)
    print(f"Start Date: {start_date}")
    print(f"Date one year and one day later: {future_date}")