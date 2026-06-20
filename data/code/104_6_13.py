from datetime import datetime
DATE_FORMAT = '%Y-%m-%d'

def compare_dates(date_str1, date_str2):
    date1 = datetime.strptime(date_str1, DATE_FORMAT)
    date2 = datetime.strptime(date_str2, DATE_FORMAT)
    if date1 < date2:
        return 'date1 is earlier than date2'
    elif date1 > date2:
        return 'date1 is later than date2'
    else:
        return 'date1 and date2 are the same'
if __name__ == '__main__':
    date_a = '2023-01-15'
    date_b = '2023-03-01'
    result = compare_dates(date_a, date_b)
    print(result)
    date_c = '2024-05-20'
    date_d = '2024-03-10'
    result = compare_dates(date_c, date_d)
    print(result)