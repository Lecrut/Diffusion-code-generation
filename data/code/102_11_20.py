import calendar

def is_weekday(date_string: str) -> bool:
    year, month, day = map(int, date_string.split('-'))
    day_of_week = calendar.weekday(year, month, day)
    return day_of_week < 5

if __name__ == '__main__':
    sample_date = '2023-10-23'
    result = is_weekday(sample_date)
    print(result)