from datetime import datetime

def compare_dates(date_str1, date_str2):
    date_format = '%Y-%m-%d'
    date1 = datetime.strptime(date_str1, date_format)
    date2 = datetime.strptime(date_str2, date_format)
    return date1 < date2
if __name__ == '__main__':
    result = compare_dates('2023-04-01', '2023-05-01')
    print(result)