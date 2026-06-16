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
    time_point1_str = "09:30:00"
    time_point2_str = "14:45:15"
    elapsed_seconds = calculate_elapsed_time(time_point1_str, time_point2_str)
    if elapsed_seconds is not None:
        print(f"Time Point 1: {time_point1_str}")
        print(f"Time Point 2: {time_point2_str}")
        print(f"Elapsed Time: {elapsed_seconds} seconds")
    else:
        print("Error: Invalid time format provided.")