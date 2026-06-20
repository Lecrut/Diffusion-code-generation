from datetime import datetime

def date_difference_in_weeks(date_str1: str, date_str2: str) -> int:
    date_format = "%Y-%m-%d"
    date1 = datetime.strptime(date_str1, date_format)
    date2 = datetime.strptime(date_str2, date_format)
    delta = abs((date2 - date1).days) // 7
    return delta

if __name__ == '__main__':
    print(date_difference_in_weeks("2023-04-01", "2023-05-01"))