import datetime
def calculate_future_date(start_date_str, days):
    try:
        start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d").date()
        future_date = start_date + datetime.timedelta(days=days)
        return future_date.strftime("%Y-%m-%d")
    except ValueError:
        return "Error: Invalid date format. Please use YYYY-MM-DD."
if __name__ == '__main__':
    sample_date = "2023-10-26"
    sample_days = 10
    result = calculate_future_date(sample_date, sample_days)
    print(f"Start Date: {sample_date}")
    print(f"Days to Add: {sample_days}")
    print(f"Next Upcoming Date: {result}")