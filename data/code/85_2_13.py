from datetime import datetime, timedelta

def weeks_difference(date_str1, date_str2):
    format_str = "%Y-%m-%d"
    date1 = datetime.strptime(date_str1, format_str)
    date2 = datetime.strptime(date_str2, format_str)
    delta = abs((date2 - date1).days) // 7
    return delta

if __name__ == '__main__':
    print(weeks_difference("2023-01-01", "2023-01-15"))