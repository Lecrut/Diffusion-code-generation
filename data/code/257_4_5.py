from datetime import datetime

def date_difference(date_str1, date_str2):
    date_format = '%Y-%m-%d'
    date1 = datetime.strptime(date_str1, date_format)
    date2 = datetime.strptime(date_str2, date_format)
    return abs((date2 - date1).days)

if __name__ == '__main__':
    start_date = '2023-04-01'
    end_date = '2023-05-01'
    result = date_difference(start_date, end_date)
    print(result)