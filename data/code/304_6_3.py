import datetime
def compare_iso_dates(date1_str, date2_str):
    date1 = datetime.datetime.strptime(date1_str, '%Y-%m-%d')
    date2 = datetime.datetime.strptime(date2_str, '%Y-%m-%d')
    return date1 < date2
if __name__ == '__main__':
    date_a = "2023-01-15"
    date_b = "2023-01-20"
    result1 = compare_iso_dates(date_a, date_b)
    print(f"{date_a} precedes {date_b}: {result1}")
    date_c = "2024-05-01"
    date_d = "2024-04-30"
    result2 = compare_iso_dates(date_c, date_d)
    print(f"{date_c} precedes {date_d}: {result2}")
    date_e = "1999-12-31"
    date_f = "2000-01-01"
    result3 = compare_iso_dates(date_e, date_f)
    print(f"{date_e} precedes {date_f}: {result3}")
    date_g = "2025-01-01"
    date_h = "2025-01-01"
    result4 = compare_iso_dates(date_g, date_h)
    print(f"{date_g} precedes {date_h}: {result4}")