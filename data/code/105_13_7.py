import datetime
def calculate_future_date(current_date_str, days_to_add):
    try:
        current_date = datetime.datetime.strptime(current_date_str, "%Y-%m-%d").date()
        future_date = current_date + datetime.timedelta(days=days_to_add)
        return future_date.strftime("%Y-%m-%d")
    except ValueError:
        return "Error: Invalid date format. Please use YYYY-MM-DD."
if __name__ == '__main__':
    current_date_input = "2023-10-26"
    days_input = 15
    result = calculate_future_date(current_date_input, days_input)
    print(f"Current Date: {current_date_input}")
    print(f"Days to Add: {days_input}")
    print("-" * 30)
    print(f"Next Upcoming Date: {result}")