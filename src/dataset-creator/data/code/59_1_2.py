import datetime
def get_weekday_name(date_input):
    try:
        if isinstance(date_input, str):
            date_obj = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()
        elif isinstance(date_input, datetime.date) or isinstance(date_input, datetime.datetime):
            date_obj = (datetime.date if not hasattr(date_input, 'year') else datetime.datetime).replace(year=date_input.year, month=date_input.month, day=date_input.day) if isinstance(date_input, datetime.datetime) else date_input
        else:
            raise ValueError("Input must be a string in format YYYY-MM-DD or a date object.")
        weekday_name = date_obj.strftime("%A")
    except (ValueError, TypeError):
        return None
if __name__ == '__main__':
    sample_inputs = ["2023-10-05", "2024-06-17", "invalid-date"]
    for input_val in sample_inputs:
        result = get_weekday_name(input_val)
        print(f"Input: {input_val} -> Weekday: {result}")