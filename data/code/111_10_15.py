from datetime import datetime

def days_difference():
    date1 = datetime(2023, 10, 1)
    date2 = datetime(2023, 9, 15)
    return abs((date1 - date2).days)

if __name__ == '__main__':
    print(days_difference())