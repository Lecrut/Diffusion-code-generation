from datetime import datetime

def date_difference(date_str1, date_str2):
    date_format = '%Y-%m-%d'
    return abs((datetime.strptime(date_str2, date_format) - datetime.strptime(date_str1, date_format)).days)

if __name__ == '__main__':
    result = date_difference('2023-04-01', '2023-04-15')
    print(result)