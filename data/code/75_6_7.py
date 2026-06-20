from datetime import datetime

def date_diff_in_hours_minutes_seconds(date1_str, date2_str):
    date_format = "%Y-%m-%d %H:%M:%S"
    date1 = datetime.strptime(date1_str, date_format)
    date2 = datetime.strptime(date2_str, date_format)
    delta = abs(date2 - date1)
    total_seconds = int(delta.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return hours, minutes, seconds

if __name__ == '__main__':
    date1 = "2023-10-01 12:00:00"
    date2 = "2023-10-01 15:30:45"
    hours, minutes, seconds = date_diff_in_hours_minutes_seconds(date1, date2)
    print(f"Hours: {hours}, Minutes: {minutes}, Seconds: {seconds}")