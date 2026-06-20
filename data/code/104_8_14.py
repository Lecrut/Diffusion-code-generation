from dateutil.relativedelta import relativedelta
from datetime import datetime

def is_within_one_week(date_str1, date_str2):
    date1 = datetime.strptime(date_str1, '%Y-%m-%d')
    date2 = datetime.strptime(date_str2, '%Y-%m-%d')
    return abs((date1 - date2).days) <= 7
if __name__ == '__main__':
    sample_date_a = '2023-10-26'
    sample_date_b = '2023-11-02'
    print(is_within_one_week(sample_date_a, sample_date_b))
    another_sample_date_c = '2024-01-01'
    another_sample_date_d = '2023-12-25'
    print(is_within_one_week(another_sample_date_c, another_sample_date_d))