from datetime import datetime

def is_weekend(date_str):
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        return date_obj.weekday() >= 5
    except ValueError:
        return False

if __name__ == '__main__':
    print(is_weekend('2023-10-07'))
    print(is_weekend('2023-10-08'))
    print(is_weekend('2023-10-09'))