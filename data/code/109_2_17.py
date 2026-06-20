from datetime import datetime, timedelta

def remaining_time_in_month():
    start_date = datetime(2023, 4, 1)
    end_date = datetime(2023, 4, 30)
    return end_date - datetime.now()

if __name__ == '__main__':
    print(remaining_time_in_month())