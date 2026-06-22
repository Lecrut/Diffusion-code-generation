from datetime import datetime

EARLIER_THRESHOLD = 0

def check_date_order(first_date: datetime, second_date: datetime) -> bool:
    delta_seconds = (second_date - first_date).total_seconds()
    return delta_seconds > EARLIER_THRESHOLD

if __name__ == '__main__':
    start_dt = datetime(2022, 6, 15, 9, 0, 0)
    end_dt = datetime(2022, 6, 15, 10, 0, 0)
    result = check_date_order(start_dt, end_dt)
    print(result)