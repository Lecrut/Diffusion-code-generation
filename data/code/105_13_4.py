import datetime
def calculate_future_date(start_date_str, days_to_add_str):
    try:
        start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d").date()
        days_to_add = int(days_to_add_str)
        future_date = start_date + datetime.timedelta(days=days_to_add)
        return future_date.strftime("%Y-%m-%d")
    except ValueError:
        return "Error: Invalid date format. Please use YYYY-MM-DD."
    except ValueError:
        return "Error: Invalid number of days. Please enter an integer."
if __name__ == '__main__':
    start_date = "2023-10-26"
    days = "10"
    result = calculate_future_date(start_date, days)
    print(f"Start Date: {start_date}")
    print(f"Days to Add: {days}")
    print(f"Next Upcoming Date: {result}")