import datetime
def calculate_time_difference(start_time_str, end_time_str):
    try:
        start_time = datetime.datetime.fromisoformat(start_time_str)
        end_time = datetime.datetime.fromisoformat(end_time_str)
        if end_time >= start_time:
            difference = end_time - start_time
            return difference
        else:
            return - (start_time - end_time)
    except ValueError as e:
        return f"Error parsing date: {e}"
    except TypeError:
        return "Error: Input must be strings"
if __name__ == '__main__':
    start = "2023-01-01T10:00:00"
    end = "2023-01-01T11:30:00"
    result = calculate_time_difference(start, end)
    print(result)
    start_reversed = "2023-01-01T11:30:00"
    end_reversed = "2023-01-01T10:00:00"
    result_reversed = calculate_time_difference(start_reversed, end_reversed)
    print(result_reversed)
    invalid_start = "2023/01/01 10:00:00"
    end_invalid = "2023-01-01T11:00:00"
    result_error = calculate_time_difference(invalid_start, end_invalid)
    print(result_error)