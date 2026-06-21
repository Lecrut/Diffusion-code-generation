from datetime import date

class DateChecker:
    REFERENCE_YEAR = 2000

    @staticmethod
    def _build_date(y, m, d):
        return date(y, m, d)

    @staticmethod
    def is_same(date1, date2):
        d1 = DateChecker._build_date(*date1)
        d2 = DateChecker._build_date(*date2)
        return d1 == d2

if __name__ == '__main__':
    t1 = (2024, 12, 25)
    t2 = (2024, 12, 25)
    result = DateChecker.is_same(t1, t2)
    print(result)