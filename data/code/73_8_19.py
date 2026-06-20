from datetime import datetime

def calculate_time_difference(date_str1, date_str2):
    try:
        date_format = "%Y-%m-%d %H:%M:%S"
        date1 = datetime.strptime(date_str1, date_format)
        date2 = datetime.strptime(date_str2, date_format)
        difference = abs((date2 - date1).total_seconds())
        return f"{int(difference // 3600)} hours {int((difference % 3600) // 60)} minutes"
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD HH:MM:SS."

if __name__ == '__main__':
    print(calculate_time_difference("2023-10-01 12:00:00", "2023-10-02 14:30:00"))
    print(calculate_time_difference("2023-10-01 12:00:00", "2023-10-01 12:60:00"))