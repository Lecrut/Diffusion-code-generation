import datetime
def calculate_time_difference(dt1, dt2, unit):
    if dt1 is None or dt2 is None:
        raise ValueError("Both datetime objects must be provided.")
    if unit.lower() == 'days':
        diff = dt2 - dt1
        return diff.days
    elif unit.lower() == 'hours':
        diff = dt2 - dt1
        return diff.total_seconds() / 3600
    elif unit.lower() == 'minutes':
        diff = dt2 - dt1
        return diff.total_seconds() / 60
    elif unit.lower() == 'seconds':
        diff = dt2 - dt1
        return diff.total_seconds()
    else:
        raise ValueError("Unsupported unit. Please use 'days', 'hours', 'minutes', or 'seconds'.")
if __name__ == '__main__':
    start_time = datetime.datetime(2023, 10, 26, 10, 0, 0)
    end_time = datetime.datetime(2023, 10, 29, 14, 30, 15)
    time_unit = "hours"
    try:
        result = calculate_time_difference(start_time, end_time, time_unit)
        print(f"Start Time: {start_time}")
        print(f"End Time: {end_time}")
        print(f"Time Difference in {time_unit}: {result:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")