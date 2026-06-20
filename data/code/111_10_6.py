from datetime import datetime

def days_difference():
    date1 = datetime(2023, 9, 1)
    date2 = datetime(2023, 10, 15)
    return (date2 - date1).days

if __name__ == '__main__':
    print(days_difference())