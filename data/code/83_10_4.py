import datetime
def are_dates_equal(date_str1, date_str2):
    try:
        date1 = datetime.datetime.strptime(date_str1, '%Y-%m-%d').date()
        date2 = datetime.datetime.strptime(date_str2, '%Y-%m-%d').date()
        return date1 == date2
    except ValueError:
        return False
if __name__ == '__main__':
    date_a = "2023-10-27"
    date_b = "2023-10-27"
    date_c = "2023-10-28"
    date_d = "2023/10/27"
    date_e = "2023-10-27T10:00:00"
    print(f"Comparing {date_a} and {date_b}: {are_dates_equal(date_a, date_b)}")
    print(f"Comparing {date_a} and {date_c}: {are_dates_equal(date_a, date_c)}")
    print(f"Comparing {date_a} and {date_d} (format error): {are_dates_equal(date_a, date_d)}")
    print(f"Comparing {date_a} and {date_e} (time error): {are_dates_equal(date_a, date_e)}")
    print(f"Comparing {date_b} and {date_c}: {are_dates_equal(date_b, date_c)}")