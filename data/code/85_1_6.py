from datetime import datetime
def calculate_week_difference(date1, date2):
    diff = abs(date1 - date2)
    weeks = diff.days // 7
    return weeks
if __name__ == '__main__':
    date_a = datetime(2023, 1, 1)
    date_b = datetime(2023, 1, 8)
    result1 = calculate_week_difference(date_a, date_b)
    print(f"Difference between {date_a.date()} and {date_b.date()}: {result1} weeks")
    date_c = datetime(2023, 1, 1)
    date_d = datetime(2023, 1, 7)
    result2 = calculate_week_difference(date_c, date_d)
    print(f"Difference between {date_c.date()} and {date_d.date()}: {result2} weeks")
    date_e = datetime(2023, 1, 1)
    date_f = datetime(2023, 1, 1)
    result3 = calculate_week_difference(date_e, date_f)
    print(f"Difference between {date_e.date()} and {date_f.date()}: {result3} weeks")
    date_g = datetime(2023, 1, 1)
    date_h = datetime(2023, 1, 8)
    result4 = calculate_week_difference(date_g, date_h)
    print(f"Difference between {date_g.date()} and {date_h.date()}: {result4} weeks")