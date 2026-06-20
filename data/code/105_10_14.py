from datetime import datetime, timedelta

NEXT_DAY_OFFSET = timedelta(days=1)

def get_next_calendar_day(date_str):
    date_format = '%Y-%m-%d'
    parsed_date = datetime.strptime(date_str, date_format)
    return parsed_date + NEXT_DAY_OFFSET

if __name__ == '__main__':
    sample_date = '2023-10-05'
    print(get_next_calendar_day(sample_date))