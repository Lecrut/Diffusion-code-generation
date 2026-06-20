from datetime import datetime

def date_difference_seconds(date_str1: str, date_str2: str) -> tuple:
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
    result1 = date_difference_seconds("2023-10-01 12:00:00", "2023-10-01 14:30:45")
    print(f"Hours: {result1[0]}, Minutes: {result1[1]}, Seconds: {result1[2]}")
    result2 = date_difference_seconds("2023-11-01 09:00:00", "2023-10-31 18:45:30")
    print(f"Hours: {result2[0]}, Minutes: {result2[1]}, Seconds: {result2[2]}")