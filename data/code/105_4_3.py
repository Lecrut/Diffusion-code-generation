from datetime import date, timedelta
def add_days(start_date, days):
    future_date = start_date + timedelta(days=days)
    return future_date
if __name__ == '__main__':
    start_date_1 = date(2023, 1, 31)
    interval_1 = 10
    result_1 = add_days(start_date_1, interval_1)
    print(f"Start Date: {start_date_1}, Interval: {interval_1}, Result: {result_1}")
    start_date_2 = date(2024, 2, 28)
    interval_2 = 1
    result_2 = add_days(start_date_2, interval_2)
    print(f"Start Date: {start_date_2}, Interval: {interval_2}, Result: {result_2}")
    start_date_3 = date(2024, 2, 28)
    interval_3 = 2
    result_3 = add_days(start_date_3, interval_3)
    print(f"Start Date: {start_date_3}, Interval: {interval_3}, Result: {result_3}")
    start_date_4 = date(2023, 12, 31)
    interval_4 = 31
    result_4 = add_days(start_date_4, interval_4)
    print(f"Start Date: {start_date_4}, Interval: {interval_4}, Result: {result_4}")