from datetime import datetime

def calculate_week_difference(date1, date2):
    delta = abs(date2 - date1)
    return delta.days // 7

if __name__ == '__main__':
    date1 = datetime(2023, 1, 1)
    date2 = datetime(2023, 1, 15)
    print(calculate_week_difference(date1, date2))