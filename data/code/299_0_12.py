from datetime import datetime

def is_weekend(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    return date_obj.weekday() >= 5
if __name__ == '__main__':
    sample_date1 = '2023-10-14'
    sample_date2 = '2023-10-15'
    print(is_weekend(sample_date1))
    print(is_weekend(sample_date2))