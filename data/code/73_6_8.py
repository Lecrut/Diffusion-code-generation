from datetime import datetime

def date_difference(date_str1, date_str2):
    format_str = "%Y-%m-%d %H:%M:%S"
    date_obj1 = datetime.strptime(date_str1, format_str)
    date_obj2 = datetime.strptime(date_str2, format_str)
    return abs((date_obj2 - date_obj1).total_seconds())

if __name__ == '__main__':
    print(date_difference("2023-04-01 12:00:00", "2023-04-02 12:00:00"))