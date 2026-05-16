import datetime
def calculate_future_date(start_date, days_to_add):
    future_date = start_date + datetime.timedelta(days=days_to_add)
    return future_date
if __name__ == '__main__':
    start_date_str = "2023-10-26"
    days_to_add_val = 45
    try:
        start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d").date()
        future_date = calculate_future_date(start_date, days_to_add_val)
        print(f"Start Date: {start_date}")
        print(f"Days to Add: {days_to_add_val}")
        print(f"Future Date: {future_date}")
    except ValueError as e:
        print(f"Error processing date: {e}")