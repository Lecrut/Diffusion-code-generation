from datetime import date, timedelta

def time_left_in_month(start_date=date(2023, 4, 1), end_date=date(2023, 5, 1)):
    return (end_date - start_date).days

if __name__ == '__main__':
    print(time_left_in_month())