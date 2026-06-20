from datetime import datetime

def calculate_time_difference(date_str1, date_str2):
    try:
        date_format = "%Y-%m-%d %H:%M:%S"
        date1 = datetime.strptime(date_str1, date_format)
        date2 = datetime.strptime(date_str2, date_format)
        difference = abs((date2 - date1).total_seconds())
        return difference
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD HH:MM:SS."

if __name__ == '__main__':
    result = calculate_time_difference("2023-10-05 14:30:00", "2023-10-05 16:45:00")
    print(result)
    result = calculate_time_difference("2023-10-05 14:30:00", "2023-10-05 16:45")
    print(result)