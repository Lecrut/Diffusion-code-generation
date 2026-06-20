from datetime import datetime

def days_difference(date_str1, date_str2):
    format_str = "%Y-%m-%d"
    a = datetime.strptime(date_str1, format_str)
    b = datetime.strptime(date_str2, format_str)
    delta = abs((b - a).days)
    return delta

if __name__ == '__main__':
    print(days_difference("2023-01-01", "2023-01-15"))