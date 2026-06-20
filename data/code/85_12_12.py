from datetime import datetime

def calculate_week_difference(start_date, end_date):
    delta = end_date - start_date
    return delta.days // 7

if __name__ == '__main__':
    start = datetime(2023, 1, 1)
    end = datetime(2023, 1, 15)
    print(calculate_week_difference(start, end))