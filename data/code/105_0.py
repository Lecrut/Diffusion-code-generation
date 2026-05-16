import datetime
def calculate_future_date(start_date):
    start = datetime.date(start_date.year, start_date.month, start_date.day)
    future_date = start + datetime.timedelta(days=30)
    return future_date
if __name__ == '__main__':
    start_date_str = "2023-02-28"
    start_date = datetime.date(int(start_date_str.split('-')[0]), int(start_date_str.split('-')[1]), int(start_date_str.split('-')[2]))
    future_date = calculate_future_date(start_date)
    print(future_date.strftime("%Y-%m-%d"))