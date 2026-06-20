from datetime import datetime

def calculate_days(date_str1, date_str2):
    date_format = "%Y-%m-%d"
    date1 = datetime.strptime(date_str1, date_format)
    date2 = datetime.strptime(date_str2, date_format)
    return abs((date2 - date1).days)

if __name__ == '__main__':
    print(calculate_days('2023-01-01', '2023-01-31'))