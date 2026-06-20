from datetime import datetime, timedelta

def weeks_difference(date_str1: str, date_str2: str) -> int:
    date_format = "%Y-%m-%d"
    date1 = datetime.strptime(date_str1, date_format)
    date2 = datetime.strptime(date_str2, date_format)
    difference = abs((date2 - date1).days) // 7
    return difference

if __name__ == '__main__':
    print(weeks_difference("2023-01-01", "2023-02-01"))