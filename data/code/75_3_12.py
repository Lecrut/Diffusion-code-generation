from datetime import datetime, timedelta

def date_difference(date_str1, date_str2):
    date_format = '%Y-%m-%d'
    date1 = datetime.strptime(date_str1, date_format)
    date2 = datetime.strptime(date_str2, date_format)
    return abs(date1 - date2)

if __name__ == '__main__':
    print(date_difference('2023-04-01', '2023-03-15'))