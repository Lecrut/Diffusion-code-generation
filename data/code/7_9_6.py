import datetime
def calculate_time_difference(dt1, dt2, unit):
    difference = abs(dt1 - dt2)
    if unit == 'days':
        return difference.days
    elif unit == 'hours':
        return int(difference.total_seconds() // 3600)
    elif unit == 'minutes':
        return int(difference.total_seconds() // 60)
    elif unit == 'seconds':
        return int(difference.total_seconds())
    else:
        raise ValueError("Unsupported unit specified. Choose 'days', 'hours', 'minutes', or 'seconds'.")
if __name__ == '__main__':
    start_time = datetime.datetime(2023, 10, 26, 10, 30, 0)
    end_time = datetime.datetime(2023, 10, 28, 14, 45, 15)
    time_unit = 'hours'
    try:
        result = calculate_time_difference(start_time, end_time, time_unit)
        print(f"Start Time: {start_time}")
        print(f"End Time: {end_time}")
        print(f"Time Difference in {time_unit}: {result}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")