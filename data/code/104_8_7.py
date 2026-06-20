from dateutil.relativedelta import relativedelta

def is_within_one_week(date_str1, date_str2):
    from datetime import datetime
    date_format = '%Y-%m-%d'
    date1 = datetime.strptime(date_str1, date_format)
    date2 = datetime.strptime(date_str2, date_format)
    
    if abs((date1 - date2).days) <= 7:
        return True
    else:
        return False

if __name__ == '__main__':
    sample_dates = {
        '2023-10-26': '2023-10-20',
        '2024-01-01': '2023-12-31'
    }
    
    for date_a, date_b in sample_dates.items():
        result = is_within_one_week(date_a, date_b)
        print(f'{date_a} within one week of {date_b}: {result}')