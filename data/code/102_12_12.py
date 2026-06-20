import datetime

def is_weekday(date_str):
    if not isinstance(date_str, str):
        raise TypeError('Input must be a string')
    try:
        date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
        return date_obj.weekday() < 5
    except ValueError:
        raise ValueError('Invalid date format. Please use YYYY-MM-DD')
if __name__ == '__main__':
    print(is_weekday('2023-10-06'))
    print(is_weekday('2023-10-07'))