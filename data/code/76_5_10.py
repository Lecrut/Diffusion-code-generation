from datetime import datetime

def days_difference(date1, date2):
    return abs((date2 - date1).days)

if __name__ == '__main__':
    date1 = datetime(2023, 10, 1)
    date2 = datetime(2023, 10, 15)
    print(days_difference(date1, date2))