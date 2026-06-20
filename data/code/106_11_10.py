from datetime import datetime

def year_difference(date_str1, date_str2):
    date_format = "%Y-%m-%d"
    date1 = datetime.strptime(date_str1, date_format)
    date2 = datetime.strptime(date_str2, date_format)
    return abs((date2 - date1).days) // 365

if __name__ == '__main__':
    print(year_difference('2020-01-01', '2023-04-15'))