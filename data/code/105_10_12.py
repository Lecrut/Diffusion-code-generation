from datetime import datetime, timedelta

def next_calendar_day(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    next_day = date_obj + timedelta(days=1)
    return next_day

if __name__ == '__main__':
    sample_date = '2023-10-05'
    print(next_calendar_day(sample_date))