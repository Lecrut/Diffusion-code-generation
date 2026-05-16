import datetime
if __name__ == '__main__':
    start_time_str = "09:00:00"
    end_time_str = "17:30:00"
    start_time = datetime.datetime.strptime(start_time_str, "%H:%M:%S")
    end_time = datetime.datetime.strptime(end_time_str, "%H:%M:%S")
    time_difference = end_time - start_time
    total_seconds = time_difference.total_seconds()
    total_hours = total_seconds / 3600.0
    print(f"{total_hours}")