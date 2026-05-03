import datetime
def calculate_time_difference(dt1, dt2, unit):
    if dt1 is None or dt2 is None:
        raise ValueError("Both datetime objects must be provided.")
    if unit.lower() == 'days':
        difference = abs(dt1 - dt2)
        result = difference.days
        return result
    elif unit.lower() == 'hours':
        difference = abs(dt1 - dt2)
        result = difference.total_seconds() / 3600
        return result
    elif unit.lower() == 'minutes':
        difference = abs(dt1 - dt2)
        result = difference.total_seconds() / 60
        return result
    elif unit.lower() == 'seconds':
        difference = abs(dt1 - dt2)
        result = difference.total_seconds()
        return result
    else:
        raise ValueError("Unsupported unit specified. Supported units are: days, hours, minutes, seconds.")
if __name__ == '__main__':
    date1 = datetime.datetime(2023, 10, 26, 10, 0, 0)
    date2 = datetime.datetime(2023, 10, 28, 14, 30, 15)
    time_unit = "hours"
    try:
        result = calculate_time_difference(date1, date2, time_unit)
        print(f"Time difference between {date1} and {date2} in {time_unit}: {result}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")