from datetime import datetime

def weeks_difference(date1, date2):
    delta = abs((date2 - date1).days)
    return delta // 7

if __name__ == '__main__':
    date1 = datetime(2023, 1, 1)
    date2 = datetime(2023, 2, 14)
    print(weeks_difference(date1, date2))