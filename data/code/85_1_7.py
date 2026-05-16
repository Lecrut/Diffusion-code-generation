import datetime
def calculate_week_difference(date1, date2):
    diff = abs(date1 - date2)
    weeks = diff.days // 7
    return weeks
if __name__ == '__main__':
    date_a = datetime.datetime(2023, 1, 1, 10, 0, 0)
    date_b = datetime.datetime(2023, 1, 15, 12, 0, 0)
    date_c = datetime.datetime(2023, 1, 1, 10, 0, 0)
    date_d = datetime.datetime(2023, 1, 8, 9, 0, 0)
    date_e = datetime.datetime(2023, 1, 7, 10, 0, 0)
    print(f"Difference between {date_a} and {date_b}: {calculate_week_difference(date_a, date_b)} weeks")
    print(f"Difference between {date_c} and {date_d}: {calculate_week_difference(date_c, date_d)} weeks")
    print(f"Difference between {date_a} and {date_c}: {calculate_week_difference(date_a, date_c)} weeks")
    print(f"Difference between {date_d} and {date_e}: {calculate_week_difference(date_d, date_e)} weeks")