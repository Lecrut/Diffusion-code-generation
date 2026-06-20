import datetime

def validate_date(date_str):
    try:
        year, month, day = map(int, date_str.split('-'))
        return datetime.date(year, month, day)
    except ValueError:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")

def get_weekday(date_str):
    date_object = validate_date(date_str)
    return date_object.weekday()

if __name__ == '__main__':
    sample_date = '2024-07-04'
    weekday_index = get_weekday(sample_date)
    print(weekday_index)