from datetime import datetime

def weeks_between_dates(date_str1: str, date_str2: str) -> int:
    date_format = '%Y-%m-%d'
    date1 = datetime.strptime(date_str1, date_format)
    date2 = datetime.strptime(date_str2, date_format)
    delta = abs((date2 - date1).days // 7)
    return delta
if __name__ == '__main__':
    print(weeks_between_dates('2023-01-01', '2023-01-15'))
    print(weeks_between_dates('2023-02-01', '2023-03-01'))