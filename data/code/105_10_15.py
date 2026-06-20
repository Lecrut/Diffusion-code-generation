from datetime import datetime, timedelta

def get_next_calendar_day(date_str):
    date_format = '%Y-%m-%d'
    parsed_date = datetime.strptime(date_str, date_format)
    next_day = parsed_date + timedelta(days=1)
    return next_day

if __name__ == '__main__':
    sample_date = '2023-09-20'
    result = get_next_calendar_day(sample_date)
    print(result)