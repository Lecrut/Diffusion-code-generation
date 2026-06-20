import datetime

def get_next_weekday(start_date_str, target_weekday):
    start_date = datetime.datetime.strptime(start_date_str, '%Y-%m-%d').date()
    current_day = start_date.day
    current_month = start_date.month
    current_year = start_date.year
    while True:
        if start_date.weekday() == target_weekday:
            return start_date.strftime('%Y-%m-%d')
        start_date += datetime.timedelta(days=1)
if __name__ == '__main__':
    reference_date = '2023-10-01'
    target_day = 4
    result = get_next_weekday(reference_date, target_day)
    print(result)