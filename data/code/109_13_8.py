import datetime

def days_left_in_month(start_date):
    if start_date.month == 12:
        return 31 - start_date.day
    elif start_date.month in {1, 3, 5, 7, 8, 10, 12}:
        return 31 - start_date.day
    else:
        return 30 - start_date.day

if __name__ == '__main__':
    sample_start_date = datetime.date(2023, 10, 15)
    print(days_left_in_month(sample_start_date))