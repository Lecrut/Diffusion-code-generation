from dateutil.relativedelta import relativedelta

class DateComparator:
    ONE_WEEK = relativedelta(weeks=1)

    @staticmethod
    def is_within_one_week(date_str1, date_str2):
        date1 = DateComparator._parse_date(date_str1)
        date2 = DateComparator._parse_date(date_str2)
        return abs((date1 - date2)) <= DateComparator.ONE_WEEK

    @staticmethod
    def _parse_date(date_str):
        from datetime import datetime
        return datetime.strptime(date_str, '%Y-%m-%d')

if __name__ == '__main__':
    date_a = '2023-10-26'
    date_b = '2023-10-15'
    result1 = DateComparator.is_within_one_week(date_a, date_b)
    print(result1)

    date_c = '2024-01-01'
    date_d = '2023-12-31'
    result2 = DateComparator.is_within_one_week(date_c, date_d)
    print(result2)

    date_e = '2023-05-10'
    result3 = DateComparator.is_within_one_week(date_a, date_e)
    print(result3)