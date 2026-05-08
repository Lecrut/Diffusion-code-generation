import datetime
def compare_dates(date_str1, date_str2):
    try:
        date1 = datetime.datetime.strptime(date_str1, '%Y-%m-%d')
        date2 = datetime.datetime.strptime(date_str2, '%Y-%m-%d')
        if date1 == date2:
            return "The dates are identical."
        elif date1 > date2:
            return "Date 1 is after Date 2."
        else:
            return "Date 1 is before Date 2."
    except ValueError:
        return "Error: One or both date strings are in an invalid format. Please use YYYY-MM-DD."
if __name__ == '__main__':
    date_a = "2023-10-26"
    date_b = "2023-10-26"
    print(f"Comparing {date_a} and {date_b}: {compare_dates(date_a, date_b)}")
    date_c = "2024-01-15"
    date_d = "2023-12-31"
    print(f"Comparing {date_c} and {date_d}: {compare_dates(date_c, date_d)}")
    date_e = "2025-05-01"
    date_f = "2025-05-02"
    print(f"Comparing {date_e} and {date_f}: {compare_dates(date_e, date_f)}")
    date_g = "2023/10/26"
    date_h = "2023-10-26"
    print(f"Comparing {date_g} and {date_h}: {compare_dates(date_g, date_h)}")