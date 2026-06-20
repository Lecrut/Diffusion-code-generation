import datetime

def compare_dates(date_str1: str, date_str2: str) -> int:
    date_format = '%Y-%m-%d'
    date1 = datetime.datetime.strptime(date_str1, date_format).date()
    date2 = datetime.datetime.strptime(date_str2, date_format).date()
    
    if date1 < date2:
        return -1
    elif date1 > date2:
        return 1
    else:
        return 0

if __name__ == '__main__':
    sample_date_1 = '2023-07-15'
    sample_date_2 = '2023-08-10'
    
    result = compare_dates(sample_date_1, sample_date_2)
    print(result)