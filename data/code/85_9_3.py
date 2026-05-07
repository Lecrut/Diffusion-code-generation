import datetime
def date_difference_in_weeks(date1, date2):
    diff = abs(date1 - date2)
    weeks = diff.days / 7
    return int(round(weeks))
if __name__ == '__main__':
    date_a = datetime.date(2023, 1, 1)
    date_b = datetime.date(2023, 1, 15)
    result1 = date_difference_in_weeks(date_a, date_b)
    print(f"Difference between {date_a} and {date_b}: {result1} weeks")
    date_c = datetime.date(2023, 1, 15)
    date_d = datetime.date(2022, 1, 1)
    result2 = date_difference_in_weeks(date_c, date_d)
    print(f"Difference between {date_c} and {date_d}: {result2} weeks")
    date_e = datetime.date(2024, 5, 1)
    date_f = datetime.date(2024, 4, 1)
    result3 = date_difference_in_weeks(date_e, date_f)
    print(f"Difference between {date_e} and {date_f}: {result3} weeks")