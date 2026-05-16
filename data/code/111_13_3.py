import datetime
def calculate_future_date(date_string):
    date_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d').date()
    future_date = date_obj + datetime.timedelta(days=30)
    return future_date.strftime('%Y-%m-%d')
if __name__ == '__main__':
    input_date = "2023-12-15"
    result = calculate_future_date(input_date)
    print(result)