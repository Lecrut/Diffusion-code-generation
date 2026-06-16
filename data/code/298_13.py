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
    time_point_a = "09:30:00"
    time_point_b = "14:45:30"
    elapsed_time = calculate_time_difference(time_point_a, time_point_b)
    if elapsed_time is not None:
        print(f"{time_point_a} to {time_point_b}: {elapsed_time} seconds")
    else:
        print("Error: Invalid time format provided.")