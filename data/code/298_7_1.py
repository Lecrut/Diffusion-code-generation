import datetime
if __name__ == '__main__':
    time_input = "09:30 17:45"
    parts = time_input.split()
    time1_str = parts[0]
    time2_str = parts[1]
    time1 = datetime.datetime.strptime(time1_str, "%H:%M")
    time2 = datetime.datetime.strptime(time2_str, "%H:%M")
    difference = time2 - time1
    total_seconds = difference.total_seconds()
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    print(f"Time difference: {hours} hours and {minutes} minutes")