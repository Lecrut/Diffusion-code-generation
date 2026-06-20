from datetime import datetime
DATE_FORMAT = '%Y-%m-%d'

def date_difference(date_str1, date_str2):
    date1 = datetime.strptime(date_str1, DATE_FORMAT)
    date2 = datetime.strptime(date_str2, DATE_FORMAT)
    return abs(date2 - date1)
if __name__ == '__main__':
    date1 = '2023-01-01'
    date2 = '2022-12-31'
    difference = date_difference(date1, date2)
    print(difference)