import datetime
def compare_dates(date_str1: str, date_str2: str) -> bool:
    try:
        date1 = datetime.datetime.strptime(date_str1, '%Y-%m-%d')
        date2 = datetime.datetime.strptime(date_str2, '%Y-%m-%d')
        return date1 < date2
    except ValueError:
        raise ValueError("Invalid date format provided. Expected 'YYYY-MM-DD'.")
if __name__ == '__main__':
    date_a = "2023-10-26"
    date_b = "2023-10-27"
    print(f"{date_a} precedes {date_b}: {compare_dates(date_a, date_b)}")
    date_c = "2024-01-01"
    date_d = "2023-12-31"
    print(f"{date_c} precedes {date_d}: {compare_dates(date_c, date_d)}")
    date_e = "2025-05-15"
    date_f = "2025-05-15"
    print(f"{date_e} precedes {date_f}: {compare_dates(date_e, date_f)}")
    date_g = "2023-11-01"
    date_h = "2023-11-01"
    print(f"{date_g} precedes {date_h}: {compare_dates(date_g, date_h)}")