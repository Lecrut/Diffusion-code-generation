from datetime import datetime, timedelta

def find_next_wednesday(start_date):
    current_day = start_date
    while True:
        if current_day.weekday() == 2:
            return current_day
        current_day += timedelta(days=1)
if __name__ == '__main__':
    sample_date_str = '2023-10-15'
    sample_date = datetime.strptime(sample_date_str, '%Y-%m-%d')
    next_wednesday = find_next_wednesday(sample_date)
    print(next_wednesday.strftime('%Y-%m-%d'))