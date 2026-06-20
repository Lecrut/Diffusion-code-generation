def calculate_time_difference(start_time_str, end_time_str):
    time_format = "%H:%M:%S"
    try:
        start_time = datetime.datetime.strptime(start_time_str, time_format)
        end_time = datetime.datetime.strptime(end_time_str, time_format)
        if end_time < start_time:
            raise ValueError("End time must be later than start time")
        elapsed_time = end_time - start_time
        total_seconds = elapsed_time.total_seconds()
        total_hours = total_seconds / 3600.0
        return total_hours
    except ValueError as e:
        print(f"Invalid input: {e}")
        return None

if __name__ == '__main__':
    start_time_str = "09:00:00"
    end_time_str = "17:30:00"
    elapsed = calculate_time_difference(start_time_str, end_time_str)
    print(f"{elapsed}")