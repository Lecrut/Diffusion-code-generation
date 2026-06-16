import datetime
def calculate_elapsed_time(time_str1, time_str2):
    time_format = '%H:%M:%S'
    try:
        time1 = datetime.datetime.strptime(time_str1, time_format)
        time2 = datetime.datetime.strptime(time_str2, time_format)
        elapsed = abs(time2 - time1)
        return elapsed.total_seconds()
    except ValueError:
        return None
if __name__ == '__main__':
    time_point1 = "09:30:00"
    time_point2 = "14:45:30"
    elapsed_seconds = calculate_elapsed_time(time_point1, time_point2)
    if elapsed_seconds is not None:
        print(f"{time_point1} to {time_point2}: {elapsed_seconds} seconds")
    else:
        print("Invalid time format provided.")