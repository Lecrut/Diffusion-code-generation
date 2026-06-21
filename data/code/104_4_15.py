from datetime import date

YEAR_INDEX = 0
MONTH_INDEX = 1
DAY_INDEX = 2

def is_same_date(date1: tuple, date2: tuple) -> bool:
    y1, m1, d1 = date1
    y2, m2, d2 = date2
    dt1 = date(y1, m1, d1)
    dt2 = date(y2, m2, d2)
    return dt1 == dt2

if __name__ == '__main__':
    t1 = (2023, 10, 5)
    t2 = (2023, 10, 5)
    t3 = (2023, 10, 6)
    res1 = is_same_date(t1, t2)
    res2 = is_same_date(t1, t3)
    print(res1)
    print(res2)