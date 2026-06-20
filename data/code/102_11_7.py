from datetime import datetime

def is_weekday(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d').weekday() < 5
if __name__ == '__main__':
    print(is_weekday('2023-10-06'))
    print(is_weekday('2023-10-07'))