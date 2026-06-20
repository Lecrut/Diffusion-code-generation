from datetime import datetime

def is_weekday(date_str):
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        return date_obj.weekday() < 5
    except ValueError:
        return False
if __name__ == '__main__':
    print(is_weekday('2023-10-06'))
    print(is_weekday('2023-10-07'))