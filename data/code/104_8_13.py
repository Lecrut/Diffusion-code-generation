from dateutil.relativedelta import relativedelta
from datetime import datetime

def is_within_one_week(date1_str, date2_str):
    date1 = datetime.strptime(date1_str, '%Y-%m-%d')
    date2 = datetime.strptime(date2_str, '%Y-%m-%d')
    return abs((date1 - date2).days) <= 7

if __name__ == '__main__':
    print(is_within_one_week('2023-10-01', '2023-10-08'))