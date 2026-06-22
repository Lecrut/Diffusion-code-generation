from datetime import date

YEAR_INDEX = 0
MONTH_INDEX = 1
DAY_INDEX = 2

def is_same_date(tuple1, tuple2):
    d1 = date(tuple1[YEAR_INDEX], tuple1[MONTH_INDEX], tuple1[DAY_INDEX])
    d2 = date(tuple2[YEAR_INDEX], tuple2[MONTH_INDEX], tuple2[DAY_INDEX])
    return d1 == d2

if __name__ == '__main__':
    date_a = (2024, 12, 25)
    date_b = (2024, 12, 25)
    date_c = (2025, 1, 1)
    print(is_same_date(date_a, date_b))
    print(is_same_date(date_a, date_c))