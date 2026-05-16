import datetime
def calculate_duration(date1_str, date2_str):
    date1 = datetime.datetime.strptime(date1_str, "%Y-%m-%d").date()
    date2 = datetime.datetime.strptime(date2_str, "%Y-%m-%d").date()
    if date2 > date1:
        duration = (date2 - date1).days
    else:
        duration = (date1 - date2).days
    return duration
if __name__ == '__main__':
    date_a = "2020-03-01"
    date_b = "2024-03-01"
    duration1 = calculate_duration(date_a, date_b)
    print(f"Duration between {date_a} and {date_b}: {duration1} days")
    date_c = "2020-02-29"
    date_d = "2021-03-01"
    duration2 = calculate_duration(date_c, date_d)
    print(f"Duration between {date_c} and {date_d}: {duration2} days")
    date_e = "2024-02-28"
    date_f = "2024-03-01"
    duration3 = calculate_duration(date_e, date_f)
    print(f"Duration between {date_e} and {date_f}: {duration3} days")
    date_g = "2023-12-31"
    date_h = "2024-01-01"
    duration4 = calculate_duration(date_g, date_h)
    print(f"Duration between {date_g} and {date_h}: {duration4} days")