from datetime import datetime

EARLIER_THRESHOLD = 0

def check_date_order(date_a: datetime, date_b: datetime) -> bool:
    delta = (date_b - date_a).total_seconds()
    return delta > EARLIER_THRESHOLD

if __name__ == '__main__':
    start_date = datetime(2022, 6, 1, 9, 0, 0)
    end_date = datetime(2022, 6, 1, 10, 0, 0)
    is_earlier = check_date_order(start_date, end_date)
    print(is_earlier)