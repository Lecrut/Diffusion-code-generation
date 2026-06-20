from datetime import datetime

def days_difference(date_str1, date_str2):
    format_str = "%Y-%m-%d"
    date_obj1 = datetime.strptime(date_str1, format_str)
    date_obj2 = datetime.strptime(date_str2, format_str)
    return abs((date_obj2 - date_obj1).days)

if __name__ == '__main__':
    print(days_difference("2023-01-01", "2023-01-31"))