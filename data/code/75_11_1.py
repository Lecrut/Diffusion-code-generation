import datetime
def date_difference_days(date1, date2):
    return abs((date1 - date2).days)
if __name__ == '__main__':
    date_a = datetime.datetime(2023, 1, 10, 12, 0, 0)
    date_b = datetime.datetime(2023, 1, 15, 18, 30, 0)
    result1 = date_difference_days(date_a, date_b)
    print(f"Difference between {date_a} and {date_b}: {result1} days")
    date_c = datetime.datetime(2024, 5, 1)
    date_d = datetime.datetime(2023, 12, 31)
    result2 = date_difference_days(date_c, date_d)
    print(f"Difference between {date_c} and {date_d}: {result2} days")
    date_e = datetime.datetime(2025, 1, 1)
    date_f = datetime.datetime(2025, 1, 1)
    result3 = date_difference_days(date_e, date_f)
    print(f"Difference between {date_e} and {date_f}: {result3} days")