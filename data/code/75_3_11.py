from datetime import datetime

def date_diff(date_str1, date_str2):
    date_format = '%Y-%m-%d'
    date1 = datetime.strptime(date_str1, date_format)
    date2 = datetime.strptime(date_str2, date_format)
    return abs(date2 - date1)

if __name__ == '__main__':
    print(date_diff('2023-10-01', '2023-09-15'))