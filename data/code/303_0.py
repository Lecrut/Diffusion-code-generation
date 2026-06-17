import datetime
def calculate_time_difference(start_time_str, end_time_str):
    try:
        start_time = datetime.datetime.fromisoformat(start_time_str)
        end_time = datetime.datetime.fromisoformat(end_time_str)
        if end_time >= start_time:
            time_difference = end_time - start_time
            return time_difference
        else:
            return f"Error: End time is before start time for {start_time_str} and {end_time_str}"
    except ValueError as e:
        return f"Error: Invalid ISO 8601 format provided. Details: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"
if __name__ == '__main__':
    start = "2023-01-01T10:00:00"
    end = "2023-01-01T10:30:45"
    result = calculate_time_difference(start, end)
    print(result)
    start_invalid = "2023/01/01 10:00:00"
    end_valid = "2023-01-01T10:30:45"
    result_invalid = calculate_time_difference(start_invalid, end_valid)
    print(result_invalid)
    start_reverse = "2023-01-01T10:30:45"
    end_reverse = "2023-01-01T10:00:00"
    result_reverse = calculate_time_difference(start_reverse, end_reverse)
    print(result_reverse)