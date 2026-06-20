from datetime import datetime

def months_between_dates(date_str1, date_str2):
    date_format = "%Y-%m-%d"
    date1 = datetime.strptime(date_str1, date_format)
    date2 = datetime.strptime(date_str2, date_format)
    diff = abs((date2 - date1).days)
    return (diff // 30) + ((diff % 30) > 0)

if __name__ == '__main__':
    print(months_between_dates("2022-01-01", "2023-02-15"))