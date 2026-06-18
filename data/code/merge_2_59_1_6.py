import datetime
def get_weekday_name(date_input):
    try:
        if isinstance(date_input, str):
            date_obj = datetime.datetime.strptime(date_input, "%Y-%m-%d")
        elif hasattr(date_input, 'strftime'):
            date_obj = date_input
        else:
            raise ValueError("Invalid input type. Expected string or datetime object.")
        weekday_name = date_obj.strftime("%A").capitalize()
    except (ValueError, TypeError) as e:
        return f"Error: {str(e)}"
    return weekday_name
if __name__ == '__main__':
    sample_dates = ["2023-10-05", "2024-06-17", datetime.datetime(2024, 6, 17)]
    for date in sample_dates:
        print(get_weekday_name(date))