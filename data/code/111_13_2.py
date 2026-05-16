import datetime
def calculate_future_date(date_string):
    date_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d').date()
    future_date = date_obj + datetime.timedelta(days=30)
    return future_date.strftime('%Y-%m-%d')
if __name__ == '__main__':
    sample_date = "2023-12-20"
    future_date = calculate_future_date(sample_date)
    print(future_date)