from datetime import date, timedelta

def time_left_in_month(start_date, end_date):
    return (end_date - start_date).days

if __name__ == '__main__':
    start = date(2023, 10, 1)
    end = date(2023, 10, 31)
    print(time_left_in_month(start, end))