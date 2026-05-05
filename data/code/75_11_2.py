import datetime
def date_difference_days(date1, date2):
    return abs((date1 - date2).days)
if __name__ == '__main__':
    date_a = datetime.datetime(2023, 1, 1, 10, 0, 0)
    date_b = datetime.datetime(2023, 1, 10, 15, 30, 0)
    date_c = datetime.datetime(2022, 12, 31, 23, 59, 59)
    date_d = datetime.datetime(2023, 1, 1, 0, 0, 0)
    print(f"Difference between {date_a} and {date_b}: {date_difference_days(date_a, date_b)} days")
    print(f"Difference between {date_b} and {date_a}: {date_difference_days(date_b, date_a)} days")
    print(f"Difference between {date_c} and {date_d}: {date_difference_days(date_c, date_d)} days")
    print(f"Difference between {date_d} and {date_c}: {date_difference_days(date_d, date_c)} days")