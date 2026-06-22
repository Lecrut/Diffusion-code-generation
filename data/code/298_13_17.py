import datetime

def calculate_time_difference(time_str1, time_str2):
    time_format = '%Y-%m-%d %H:%M:%S'
    try:
        time1 = datetime.datetime.strptime(time_str1, time_format)
        time2 = datetime.datetime.strptime(time_str2, time_format)
        difference = abs(time2 - time1)
        days = difference.days
        hours = difference.seconds // 3600
        minutes = (difference.seconds % 3600) // 60
        seconds = difference.seconds % 60
        return days, hours, minutes, seconds
    except ValueError:
        return None

if __name__ == '__main__':
    time_point_a = "2023-10-01 14:30:00"
    time_point_b = "2023-10-02 09:45:30"
    result = calculate_time_difference(time_point_a, time_point_b)
    if result is not None:
        days, hours, minutes, seconds = result
        print(f"{time_point_a} to {time_point_b}: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")
    else:
        print("Error: Invalid time format provided.")