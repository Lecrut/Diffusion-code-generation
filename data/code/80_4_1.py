import datetime
def is_strictly_before(date1, date2):
    return date1 < date2
if __name__ == '__main__':
    date_a = datetime.datetime(2023, 1, 1)
    date_b = datetime.datetime(2023, 1, 2)
    date_c = datetime.datetime(2023, 1, 1)
    date_d = datetime.datetime(2023, 1, 1)
    date_e = datetime.datetime(2023, 1, 3)
    print(f"Is {date_a} strictly before {date_b}? {is_strictly_before(date_a, date_b)}")
    print(f"Is {date_b} strictly before {date_a}? {is_strictly_before(date_b, date_a)}")
    print(f"Is {date_a} strictly before {date_c}? {is_strictly_before(date_a, date_c)}")
    print(f"Is {date_c} strictly before {date_a}? {is_strictly_before(date_c, date_a)}")
    print(f"Is {date_a} strictly before {date_e}? {is_strictly_before(date_a, date_e)}")
    print(f"Is {date_e} strictly before {date_a}? {is_strictly_before(date_e, date_a)}")