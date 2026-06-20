from datetime import datetime

def calculate_week_difference(date_str1, date_str2):
    date_format = '%Y-%m-%d'
    date1 = datetime.strptime(date_str1, date_format)
    date2 = datetime.strptime(date_str2, date_format)
    delta = abs((date2 - date1).days)
    weeks = delta // 7
    return weeks

if __name__ == '__main__':
    print(calculate_week_difference('2023-01-01', '2023-04-01'))