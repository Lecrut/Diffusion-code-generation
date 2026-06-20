from datetime import datetime, timedelta

def get_next_calendar_day(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    return date_obj + timedelta(days=1)

if __name__ == '__main__':
    sample_date = '2023-10-05'
    print(get_next_calendar_day(sample_date))