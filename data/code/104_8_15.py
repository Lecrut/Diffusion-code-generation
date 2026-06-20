from dateutil.relativedelta import relativedelta

def is_within_one_week(date1, date2):
    return abs((date1 - date2).days) <= 7

if __name__ == '__main__':
    from datetime import datetime
    
    sample_date1 = datetime(2023, 4, 1)
    sample_date2 = datetime(2023, 4, 8)
    
    result = is_within_one_week(sample_date1, sample_date2)
    print(result)