from datetime import datetime

def is_weekday(date_str):
    return date_str.weekday() < 5
if __name__ == '__main__':
    print(is_weekday('2023-10-04'))
    print(is_weekday('2023-10-06'))