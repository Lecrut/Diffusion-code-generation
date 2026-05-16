import datetime
def calculate_future_date(current_date_str, days_to_add):
    try:
        current_date = datetime.datetime.strptime(current_date_str, "%Y-%m-%d").date()
        days_to_add = int(days_to_add)
        if days_to_add < 0:
            raise ValueError("Number of days cannot be negative")
        future_date = current_date + datetime.timedelta(days=days_to_add)
        return future_date.strftime("%Y-%m-%d")
    except ValueError as e:
        return f"Error: Invalid input. {e}"
    except ValueError:
        return "Error: Invalid date format. Please use YYYY-MM-DD."
if __name__ == '__main__':
    current_date_input = "2023-10-26"
    days_input = "10"
    result = calculate_future_date(current_date_input, days_input)
    print(f"Current Date: {current_date_input}")
    print(f"Days to Add: {days_input}")
    print(f"Next Upcoming Date: {result}")