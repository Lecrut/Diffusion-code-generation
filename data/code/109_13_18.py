import datetime

def days_left_in_month():
    start_date = datetime.date(2023, 10, 15)
    end_date = datetime.date(2023, 11, 14)
    return (end_date - start_date).days

if __name__ == '__main__':
    print(days_left_in_month())