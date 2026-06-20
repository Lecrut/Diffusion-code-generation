from datetime import datetime

def months_between_dates(date_str1, date_str2):
    date_format = "%Y-%m-%d"
    date1 = datetime.strptime(date_str1, date_format)
    date2 = datetime.strptime(date_str2, date_format)
    delta = abs((date2 - date1).days)
    return (delta // 30) + 1

if __name__ == '__main__':
    print(months_between_dates("2022-01-01", "2022-12-31"))