from datetime import datetime, timedelta
DATE_FORMAT = '%Y-%m-%d'

def next_calendar_day(date_str):
    parsed_date = datetime.strptime(date_str, DATE_FORMAT)
    return parsed_date + timedelta(days=1)
if __name__ == '__main__':
    sample_date = '2023-10-05'
    result = next_calendar_day(sample_date)
    print(result)