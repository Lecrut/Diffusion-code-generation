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
    start = "2023-10-26T10:00:00"
    end = "2023-10-26T10:30:15"
    result = calculate_time_difference(start, end)
    print(result)
    start_reverse = "2023-10-26T10:30:15"
    end_reverse = "2023-10-26T10:00:00"
    result_reverse = calculate_time_difference(start_reverse, end_reverse)
    print(result_reverse)
    invalid_start = "2023/10/26 10:00:00"
    end_valid = "2023-10-26T10:30:15"
    result_error = calculate_time_difference(invalid_start, end_valid)
    print(result_error)