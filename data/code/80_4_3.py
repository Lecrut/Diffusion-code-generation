import datetime
def compare_dates(date1, date2):
    return date1 < date2
if __name__ == '__main__':
    date_a = datetime.datetime(2023, 1, 1)
    date_b = datetime.datetime(2023, 1, 2)
    date_c = datetime.datetime(2023, 1, 1)
    date_d = datetime.datetime(2023, 1, 1)
    date_e = datetime.datetime(2023, 1, 3)
    print(f"date_a < date_b: {compare_dates(date_a, date_b)}")
    print(f"date_b < date_a: {compare_dates(date_b, date_a)}")
    print(f"date_c < date_d: {compare_dates(date_c, date_d)}")
    print(f"date_d < date_c: {compare_dates(date_d, date_c)}")
    print(f"date_a < date_e: {compare_dates(date_a, date_e)}")
    print(f"date_e < date_a: {compare_dates(date_e, date_a)}")