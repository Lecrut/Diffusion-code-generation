from datetime import datetime

def time_difference(date_str1, date_str2):
    date_format = "%Y-%m-%d %H:%M:%S"
    date1 = datetime.strptime(date_str1, date_format)
    date2 = datetime.strptime(date_str2, date_format)
    diff = abs(date2 - date1)
    total_seconds = int(diff.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return hours, minutes, seconds

if __name__ == '__main__':
    result = time_difference("2023-10-01 12:00:00", "2023-10-01 14:30:45")
    print(f"Hours: {result[0]}, Minutes: {result[1]}, Seconds: {result[2]}")