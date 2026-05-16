import datetime
def calculate_time_difference(start_time, end_time, unit):
    difference = end_time - start_time
    if unit == 'days':
        result = difference.total_seconds() / (60 * 60 * 24)
        return result
    elif unit == 'hours':
        result = difference.total_seconds() / (60 * 60)
        return result
    elif unit == 'minutes':
        result = difference.total_seconds() / 60
        return result
    elif unit == 'seconds':
        return difference.total_seconds()
    else:
        raise ValueError("Unsupported time unit. Please use 'days', 'hours', 'minutes', or 'seconds'.")
if __name__ == '__main__':
    start = datetime.datetime(2023, 10, 26, 10, 30, 0)
    end = datetime.datetime(2023, 10, 28, 14, 45, 15)
    unit = 'hours'
    try:
        time_diff = calculate_time_difference(start, end, unit)
        print(f"Start Time: {start}")
        print(f"End Time: {end}")
        print(f"Time Difference in {unit}: {time_diff}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")