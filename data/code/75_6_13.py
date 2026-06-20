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
    return f"{hours} hours, {minutes} minutes, {seconds} seconds"

if __name__ == '__main__':
    result = time_difference("2023-10-01 12:00:00", "2023-10-01 14:30:45")
    print(result)