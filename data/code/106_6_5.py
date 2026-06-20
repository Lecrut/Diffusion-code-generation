from datetime import datetime

def calculate_age(date_str1, date_str2):
    try:
        date_format = '%Y-%m-%d'
        date1 = datetime.strptime(date_str1, date_format)
        date2 = datetime.strptime(date_str2, date_format)
        age = abs((date2 - date1).days) // 365
        return age
    except ValueError:
        return 'Invalid date format. Please use YYYY-MM-DD.'
if __name__ == '__main__':
    print(calculate_age('1990-05-15', '2023-04-30'))
    print(calculate_age('2000-01-01', '2000-12-31'))
    print(calculate_age('2010-06-20', '2015-07-21'))
    print(calculate_age('invalid-date', '2023-04-30'))