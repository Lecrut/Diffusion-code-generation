import datetime
def calculate_elapsed_time(start_time_str, end_time_str):
    time_format = "%H:%M:%S"
    start_time = datetime.datetime.strptime(start_time_str, time_format)
    end_time = datetime.datetime.strptime(end_time_str, time_format)
    if end_time < start_time:
        end_time += datetime.timedelta(days=1)
    elapsed_time = end_time - start_time
    total_seconds = elapsed_time.total_seconds()
    total_hours = total_seconds / 3600.0
    return total_hours
if __name__ == '__main__':
    start_time = "09:00:00"
    end_time = "17:30:00"
    elapsed = calculate_elapsed_time(start_time, end_time)
    print(f"{elapsed}")