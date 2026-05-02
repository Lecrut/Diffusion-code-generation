import datetime
def calculate_time_difference(dt1, dt2, unit):
    if dt1 is None or dt2 is None:
        raise ValueError("Both datetime objects must be provided.")
    if unit.lower() == 'seconds':
        diff = abs(dt1 - dt2).total_seconds()
        return diff
    elif unit.lower() == 'minutes':
        diff = abs(dt1 - dt2).total_seconds() / 60
        return diff
    elif unit.lower() == 'hours':
        diff = abs(dt1 - dt2).total_seconds() / 3600
        return diff
    elif unit.lower() == 'days':
        diff = abs(dt1 - dt2).total_seconds() / (60 * 60 * 24)
        return diff
    else:
        raise ValueError("Unsupported unit specified. Supported units are: seconds, minutes, hours, days.")
if __name__ == '__main__':
    start_time = datetime.datetime(2023, 10, 26, 10, 30, 0)
    end_time = datetime.datetime(2023, 10, 28, 14, 45, 15)
    time_unit = "hours"
    try:
        result = calculate_time_difference(start_time, end_time, time_unit)
        print(f"Start Time: {start_time}")
        print(f"End Time: {end_time}")
        print(f"Time Difference in {time_unit}: {result}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")