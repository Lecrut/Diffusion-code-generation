from datetime import datetime, timedelta

def next_calendar_day(date_str):
    current_date = datetime.strptime(date_str, '%Y-%m-%d')
    return current_date + timedelta(days=1)

if __name__ == '__main__':
    sample_date = '2023-10-05'
    print(next_calendar_day(sample_date))