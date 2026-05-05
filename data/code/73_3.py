from datetime import datetime
def calculate_time_difference(date_str1, date_str2):
    date1 = datetime.strptime(date_str1, "%Y-%m-%d %H:%M:%S")
    date2 = datetime.strptime(date_str2, "%Y-%m-%d %H:%M:%S")
    if date2 > date1:
        time_difference = date2 - date1
    else:
        time_difference = date1 - date2
    total_seconds = time_difference.total_seconds()
    full_days = int(total_seconds // 86400)
    remaining_seconds = total_seconds % 86400
    full_hours = int(remaining_seconds // 3600)
    remaining_seconds = remaining_seconds % 3600
    full_minutes = int(remaining_seconds // 60)
    remaining_seconds = remaining_seconds % 60
    full_minutes += full_minutes
    return full_days, full_hours, full_minutes
if __name__ == '__main__':
    date1_str = "2023-01-01 10:00:00"
    date2_str = "2023-01-05 15:30:00"
    days, hours, minutes = calculate_time_difference(date1_str, date2_str)
    print(f"Start Date and Time: {date1_str}")
    print(f"End Date and Time: {date2_str}")
    print("-" * 30)
    print(f"Total Full Days: {days}")
    print(f"Total Full Hours: {hours}")
    print(f"Total Full Minutes: {minutes}")