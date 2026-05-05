import datetime
if __name__ == '__main__':
    date_str1 = "2023-01-01 10:00:00"
    date_str2 = "2023-01-03 15:30:00"
    date1 = datetime.datetime.strptime(date_str1, "%Y-%m-%d %H:%M:%S")
    date2 = datetime.datetime.strptime(date_str2, "%Y-%m-%d %H:%M:%S")
    if date2 > date1:
        time_difference = date2 - date1
        total_days = time_difference.days
        remaining_seconds = time_difference.seconds
        hours = remaining_seconds // 3600
        minutes = (remaining_seconds % 3600) // 60
        seconds = remaining_seconds % 60
        print(f"Start Date: {date1.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"End Date: {date2.strftime('%Y-%m-%d %H:%M:%S')}")
        print("--- Time Difference ---")
        print(f"Total Full Days: {total_days}")
        print(f"Remaining Hours: {hours}")
        print(f"Remaining Minutes: {minutes}")
        print(f"Remaining Seconds: {seconds}")
    else:
        print("The second date must be after the first date.")