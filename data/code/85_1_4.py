import datetime
def calculate_week_difference(date1, date2):
    diff = abs(date1 - date2)
    weeks = diff.days // 7
    return weeks
if __name__ == '__main__':
    date_a = datetime.datetime(2023, 1, 1, 10, 0, 0)
    date_b = datetime.datetime(2023, 1, 15, 12, 0, 0)
    result1 = calculate_week_difference(date_a, date_b)
    print(result1)
    date_c = datetime.datetime(2023, 1, 1)
    date_d = datetime.datetime(2023, 1, 8)
    result2 = calculate_week_difference(date_c, date_d)
    print(result2)
    date_e = datetime.datetime(2022, 12, 31)
    date_f = datetime.datetime(2023, 1, 2)
    result3 = calculate_week_difference(date_e, date_f)
    print(result3)
    date_g = datetime.datetime(2024, 5, 10)
    date_h = datetime.datetime(2024, 5, 1)
    result4 = calculate_week_difference(date_g, date_h)
    print(result4)