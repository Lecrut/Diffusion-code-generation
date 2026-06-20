from datetime import datetime, timedelta

def get_next_calendar_day(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d') + timedelta(days=1)

if __name__ == '__main__':
    sample_date = '2023-12-25'
    print(get_next_calendar_day(sample_date))