from datetime import date, timedelta

def time_left_in_month(start_date=date(2023, 4, 1), end_date=date(2023, 4, 30)):
    return (end_date - start_date).days + 1

if __name__ == '__main__':
    print(time_left_in_month())