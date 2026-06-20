from datetime import datetime

def time_difference(date_str1, date_str2):
    format_str = "%Y-%m-%d %H:%M:%S"
    datetime_obj1 = datetime.strptime(date_str1, format_str)
    datetime_obj2 = datetime.strptime(date_str2, format_str)
    delta = datetime_obj2 - datetime_obj1
    total_seconds = delta.total_seconds()
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    seconds = int(total_seconds % 60)
    return f"{hours} hours, {minutes} minutes, {seconds} seconds"

if __name__ == '__main__':
    date1 = "2023-10-01 12:00:00"
    date2 = "2023-10-01 14:30:45"
    print(time_difference(date1, date2))