from datetime import datetime

date_format = '%Y-%m-%d'

def date_difference(date_str1, date_str2):
    date1 = datetime.strptime(date_str1, date_format)
    date2 = datetime.strptime(date_str2, date_format)
    return abs((date2 - date1).days)

if __name__ == '__main__':
    result = date_difference('2023-04-01', '2023-04-15')
    print(result)