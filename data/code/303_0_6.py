import datetime
def calculate_time_difference(start_time_str, end_time_str):
    try:
        start_time = datetime.datetime.fromisoformat(start_time_str)
        end_time = datetime.datetime.fromisoformat(end_time_str)
        if end_time < start_time:
            return -1, "End time is before start time"
        difference = end_time - start_time
        return difference.total_seconds(), None
    except ValueError as e:
        return None, f"Error parsing date string: {e}"
    except Exception as e:
        return None, f"An unexpected error occurred: {e}"
if __name__ == '__main__':
    start = "2023-10-26T10:00:00"
    end = "2023-10-26T10:30:15"
    seconds, error = calculate_time_difference(start, end)
    if error:
        print(f"Error calculating time difference: {error}")
    else:
        print(f"Start Time: {start}")
        print(f"End Time: {end}")
        print(f"Time Elapsed (seconds): {seconds}")