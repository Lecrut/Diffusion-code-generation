import datetime

def calculate_week_difference(date1, date2):
    difference = abs((date2 - date1).days)
    weeks = difference // 7
    return weeks
if __name__ == '__main__':
    date1 = datetime.date(2023, 1, 1)
    date2 = datetime.date(2023, 1, 8)
    print(calculate_week_difference(date1, date2))
    date1 = datetime.date(2023, 1, 1)
    date2 = datetime.date(2023, 1, 7)
    print(calculate_week_difference(date1, date2))
    date1 = datetime.date(2023, 1, 1)
    date2 = datetime.date(2023, 1, 1)
    print(calculate_week_difference(date1, date2))