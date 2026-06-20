from datetime import datetime

def calculate_week_difference(dt1, dt2):
    delta = abs(dt2 - dt1)
    return delta.days // 7

if __name__ == '__main__':
    dt1 = datetime(2023, 1, 1)
    dt2 = datetime(2023, 4, 15)
    print(calculate_week_difference(dt1, dt2))