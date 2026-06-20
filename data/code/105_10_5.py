from datetime import datetime, timedelta

def get_next_calendar_day(date_str):
    DATE_FORMAT = '%Y-%m-%d'
    parsed_date = datetime.strptime(date_str, DATE_FORMAT)
    return parsed_date + timedelta(days=1)

if __name__ == '__main__':
    sample_date = '2023-10-05'
    print(get_next_calendar_day(sample_date))