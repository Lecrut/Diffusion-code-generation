import datetime
def compare_dates(date_str1, date_str2):
    date1 = datetime.datetime.strptime(date_str1, '%Y-%m-%d').date()
    date2 = datetime.datetime.strptime(date_str2, '%Y-%m-%d').date()
    if date1 < date2:
        return date1
    else:
        return date2
if __name__ == '__main__':
    date_a = "2023-10-26"
    date_b = "2023-10-25"
    result1 = compare_dates(date_a, date_b)
    print(f"Comparing {date_a} and {date_b}: {result1}")
    date_c = "2024-01-01"
    date_d = "2023-12-31"
    result2 = compare_dates(date_c, date_d)
    print(f"Comparing {date_c} and {date_d}: {result2}")
    date_e = "1999-01-01"
    date_f = "2000-01-01"
    result3 = compare_dates(date_e, date_f)
    print(f"Comparing {date_e} and {date_f}: {result3}")