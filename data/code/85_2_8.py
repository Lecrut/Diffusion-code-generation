from datetime import datetime, timedelta

def weeks_difference(date_str1, date_str2):
    date_format = "%Y-%m-%d"
    date1 = datetime.strptime(date_str1, date_format)
    date2 = datetime.strptime(date_str2, date_format)
    delta = abs((date2 - date1).days) // 7
    return delta

if __name__ == '__main__':
    result = weeks_difference("2023-01-01", "2023-04-01")
    print(result)