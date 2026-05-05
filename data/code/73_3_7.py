import datetime
if __name__ == '__main__':
    date_str1 = "2023-01-01 10:00:00"
    date_str2 = "2023-01-05 15:30:00"
    date1 = datetime.datetime.strptime(date_str1, "%Y-%m-%d %H:%M:%S")
    date2 = datetime.datetime.strptime(date_str2, "%Y-%m-%d %H:%M:%S")
    if date2 > date1:
        time_difference = date2 - date1
        total_seconds = time_difference.total_seconds()
        full_days = int(total_seconds // 86400)
        remaining_seconds = total_seconds % 86400
        hours = int(remaining_seconds // 3600)
        remaining_seconds = remaining_seconds % 3600
        minutes = int(remaining_seconds // 60)
        seconds = int(remaining_seconds % 60)
        print(f"Start Date: {date1.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"End Date: {date2.strftime('%Y-%m-%d %H:%M:%S')}")
        print("-" * 30)
        print(f"Total Full Days: {full_days}")
        print(f"Remaining Hours: {hours}")
        print(f"Remaining Minutes: {minutes}")
        print(f"Remaining Seconds: {seconds}")
    else:
        print("Error: The second date must be after the first date.")