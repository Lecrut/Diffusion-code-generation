import datetime
if __name__ == '__main__':
    date_str1 = "2023-01-01 10:00:00"
    date_str2 = "2023-01-05 15:30:00"
    date1 = datetime.datetime.strptime(date_str1, "%Y-%m-%d %H:%M:%S")
    date2 = datetime.datetime.strptime(date_str2, "%Y-%m-%d %H:%M:%S")
    if date2 > date1:
        time_difference = date2 - date1
        total_days = time_difference.days
        remaining_seconds = time_difference.seconds
        total_hours = total_days * 24 + (remaining_seconds // 3600)
        remaining_seconds_after_hours = remaining_seconds % 3600
        total_minutes = (remaining_seconds_after_hours // 60)
        total_hours_final = total_hours % 24
        total_minutes_final = remaining_seconds_after_hours % 60
        print(f"Start Date and Time: {date1.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"End Date and Time: {date2.strftime('%Y-%m-%d %H:%M:%S')}")
        print("--------------------------------------")
        print(f"Total Full Days: {total_days}")
        print(f"Remaining Hours: {total_hours_final}")
        print(f"Remaining Minutes: {total_minutes_final}")
    else:
        print("Error: The second date must be after the first date.")