from dateutil.relativedelta import relativedelta

ONE_WEEK = relativedelta(weeks=1)

def is_within_one_week(date_str1, date_str2):
    from dateutil import parser
    date1 = parser.parse(date_str1).date()
    date2 = parser.parse(date_str2).date()
    return abs(date1 - date2) <= ONE_WEEK

if __name__ == '__main__':
    date_a = '2023-10-26'
    date_b = '2023-10-20'
    result1 = is_within_one_week(date_a, date_b)
    print(result1)

    date_c = '2024-01-01'
    date_d = '2023-12-31'
    result2 = is_within_one_week(date_c, date_d)
    print(result2)