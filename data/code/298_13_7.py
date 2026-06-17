import datetime
def calculate_time_difference(time_str1, time_str2):
    time_format = '%H:%M:%S'
    try:
        time1 = datetime.datetime.strptime(time_str1, time_format)
        time2 = datetime.datetime.strptime(time_str2, time_format)
        difference = abs(time1 - time2)
        return difference.total_seconds()
    except ValueError:
        return None
if __name__ == '__main__':
    time_point1 = "09:30:00"
    time_point2 = "14:45:30"
    elapsed_time = calculate_time_difference(time_point1, time_point2)
    if elapsed_time is not None:
        print(f"{time_point1} to {time_point2}: {elapsed_time} seconds")
    else:
        print("Error: Invalid time format provided.")