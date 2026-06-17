import datetime
def get_weekday_name(date_input):
    try:
        if isinstance(date_input, str):
            date_obj = datetime.datetime.strptime(date_input, "%Y-%m-%d")
        elif isinstance(date_input, (datetime.date, datetime.datetime)):
            date_obj = date_input.replace(hour=0, minute=0, second=0, microsecond=0)
        else:
            raise ValueError("Input must be a string in 'YYYY-MM-DD' format or a valid date object.")
        weekday_name = date_obj.strftime("%A")
    except (ValueError, TypeError):
        return "Invalid Date"
if __name__ == '__main__':
    sample_dates = ["2023-10-05", datetime.date(2024, 6, 1), "invalid-date"]
    for date_val in sample_dates:
        result = get_weekday_name(date_val)
        print(f"Input: {date_val} -> Weekday: {result}")