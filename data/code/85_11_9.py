from datetime import datetime

def weeks_between_dates(date1, date2):
    return abs((date2 - date1).days // 7)

if __name__ == '__main__':
    date1 = datetime(2023, 1, 1)
    date2 = datetime(2023, 1, 15)
    print(weeks_between_dates(date1, date2))