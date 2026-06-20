from datetime import datetime

def time_difference(date_str1, date_str2):
    format_str = "%Y-%m-%d %H:%M:%S"
    dt1 = datetime.strptime(date_str1, format_str)
    dt2 = datetime.strptime(date_str2, format_str)
    diff = dt2 - dt1
    total_seconds = diff.total_seconds()
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    seconds = int(total_seconds % 60)
    return hours, minutes, seconds

if __name__ == '__main__':
    date1 = "2023-10-01 12:00:00"
    date2 = "2023-10-01 14:30:45"
    hours, minutes, seconds = time_difference(date1, date2)
    print(f"Hours: {hours}, Minutes: {minutes}, Seconds: {seconds}")