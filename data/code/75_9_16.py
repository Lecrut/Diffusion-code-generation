from datetime import datetime

def date_difference_days(date1, date2):
    delta = abs(date2 - date1)
    return delta.days

if __name__ == '__main__':
    date1 = datetime(2023, 1, 1)
    date2 = datetime(2023, 1, 15)
    print(date_difference_days(date1, date2))