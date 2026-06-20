from datetime import datetime

def days_between_dates(date_str1, date_str2):
    date_format = '%Y-%m-%d'
    date1 = datetime.strptime(date_str1, date_format)
    date2 = datetime.strptime(date_str2, date_format)
    delta = abs((date2 - date1).days)
    return delta

if __name__ == '__main__':
    print(days_between_dates('2023-01-01', '2023-01-31'))