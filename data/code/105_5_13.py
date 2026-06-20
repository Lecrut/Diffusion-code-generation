from datetime import datetime, timedelta

def next_wednesday(start_date):
    current_day = start_date.weekday()
    days_until_next_wednesday = (2 - current_day) % 7
    next_wednesday_date = start_date + timedelta(days=days_until_next_wednesday)
    return next_wednesday_date
if __name__ == '__main__':
    sample_date_str = '2023-10-15'
    sample_date = datetime.strptime(sample_date_str, '%Y-%m-%d')
    result = next_wednesday(sample_date)
    print(result.strftime('%Y-%m-%d'))