import datetime

def is_weekday(date_str: str) -> bool:
    year, month, day = date_str.split('-')
    dt = datetime.date(int(year), int(month), int(day))
    return dt.weekday() < 5

if __name__ == '__main__':
    sample_date = '2023-10-07'
    result = is_weekday(sample_date)
    print(result)