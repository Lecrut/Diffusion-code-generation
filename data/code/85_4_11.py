from datetime import datetime

def week_difference(date1, date2):
    delta = abs((date2 - date1).days)
    return delta // 7
if __name__ == '__main__':
    date1 = datetime(2023, 1, 1)
    date2 = datetime(2023, 1, 8)
    print(week_difference(date1, date2))