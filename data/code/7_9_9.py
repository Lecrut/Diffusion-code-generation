import datetime
def calculate_time_difference(dt1, dt2, unit):
    if dt1 is None or dt2 is None:
        raise ValueError("Both datetime objects must be provided.")
    if unit == 'days':
        diff = dt2 - dt1
        result = diff.days
    elif unit == 'hours':
        diff = dt2 - dt1
        result = diff.total_seconds() / 3600
    elif unit == 'minutes':
        diff = dt2 - dt1
        result = diff.total_seconds() / 60
    else:
        raise ValueError("Unsupported unit. Please use 'days', 'hours', or 'minutes'.")
    return result
if __name__ == '__main__':
    date1 = datetime.datetime(2023, 10, 26, 10, 30, 0)
    date2 = datetime.datetime(2023, 10, 29, 15, 45, 10)
    unit = 'hours'
    try:
        time_diff = calculate_time_difference(date1, date2, unit)
        print(f"Start Date: {date1}")
        print(f"End Date: {date2}")
        print(f"Time Difference in {unit}: {time_diff}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")