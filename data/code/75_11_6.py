from datetime import datetime
def date_difference_days(date1, date2):
    diff = abs(date1 - date2)
    return diff.days
if __name__ == '__main__':
    date_a = datetime(2023, 1, 1)
    date_b = datetime(2023, 1, 10)
    result1 = date_difference_days(date_a, date_b)
    print(f"Difference between {date_a.date()} and {date_b.date()}: {result1} days")
    date_c = datetime(2024, 5, 15)
    date_d = datetime(2024, 4, 1)
    result2 = date_difference_days(date_c, date_d)
    print(f"Difference between {date_c.date()} and {date_d.date()}: {result2} days")
    date_e = datetime(2022, 12, 31)
    date_f = datetime(2023, 1, 2)
    result3 = date_difference_days(date_e, date_f)
    print(f"Difference between {date_e.date()} and {date_f.date()}: {result3} days")