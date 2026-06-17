import datetime
def calculate_time_difference(start_time_str, end_time_str):
    try:
        start_time = datetime.datetime.fromisoformat(start_time_str)
        end_time = datetime.datetime.fromisoformat(end_time_str)
        time_difference = end_time - start_time
        return time_difference
    except ValueError as e:
        return f"Error parsing date: {e}"
    except TypeError:
        return "Error: Input must be strings."
if __name__ == '__main__':
    start = "2023-01-01T10:00:00"
    end = "2023-01-01T11:30:00"
    result = calculate_time_difference(start, end)
    print(result)