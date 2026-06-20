from datetime import date, timedelta

def remaining_time_in_month():
    start_date = date(2023, 4, 1)
    end_date = date(2023, 4, 30)
    return end_date - date.today()

if __name__ == '__main__':
    print(remaining_time_in_month())