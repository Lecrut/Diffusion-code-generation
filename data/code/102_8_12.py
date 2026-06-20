from datetime import datetime
WEEKDAY_NAMES = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
IS_WEEKDAY_THRESHOLD = 5

def is_weekday(date_str):
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        day_index = date_obj.weekday()
        return day_index < IS_WEEKDAY_THRESHOLD
    except ValueError:
        return False
if __name__ == '__main__':
    print(is_weekday('2023-10-25'))
    print(is_weekday('2023-10-28'))
    print(is_weekday('2023-10-29'))