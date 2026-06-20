from datetime import datetime

def days_between_dates(date_str1, date_str2):
    date_format = "%Y-%m-%d"
    date_obj1 = datetime.strptime(date_str1, date_format)
    date_obj2 = datetime.strptime(date_str2, date_format)
    delta = abs((date_obj2 - date_obj1).days)
    return delta

if __name__ == '__main__':
    result = days_between_dates('2023-01-01', '2023-01-31')
    print(result)