import datetime
def compare_dates(date_str1, date_str2):
    try:
        date1 = datetime.datetime.strptime(date_str1, '%Y-%m-%d')
        date2 = datetime.datetime.strptime(date_str2, '%Y-%m-%d')
        return date1 < date2
    except ValueError:
        return False
if __name__ == '__main__':
    date_a = '2023-01-15'
    date_b = '2023-01-20'
    result1 = compare_dates(date_a, date_b)
    print(f"Comparing {date_a} and {date_b}: {result1}")
    date_c = '2024-05-01'
    date_d = '2024-04-30'
    result2 = compare_dates(date_c, date_d)
    print(f"Comparing {date_c} and {date_d}: {result2}")
    date_e = '1999-12-31'
    date_f = '2000-01-01'
    result3 = compare_dates(date_e, date_f)
    print(f"Comparing {date_e} and {date_f}: {result3}")
    date_g = '2025-01-01'
    date_h = '2025-01-01'
    result4 = compare_dates(date_g, date_h)
    print(f"Comparing {date_g} and {date_h}: {result4}")