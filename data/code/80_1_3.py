import datetime
def compare_dates(date_str1, date_str2):
    try:
        date1 = datetime.datetime.strptime(date_str1, '%Y-%m-%d')
        date2 = datetime.datetime.strptime(date_str2, '%Y-%m-%d')
        if date1 < date2:
            return date1
        else:
            return date2
    except ValueError:
        raise ValueError("Invalid date format provided. Dates must be in 'YYYY-MM-DD' format.")
if __name__ == '__main__':
    date_a = "2023-10-26"
    date_b = "2023-10-25"
    try:
        earlier_date = compare_dates(date_a, date_b)
        print(earlier_date)
    except ValueError as e:
        print(f"Error: {e}")
    date_c = "2024-01-01"
    date_d = "2023-12-31"
    try:
        earlier_date = compare_dates(date_c, date_d)
        print(earlier_date)
    except ValueError as e:
        print(f"Error: {e}")
    date_e = "2023-11-15"
    date_f = "2023-11-15"
    try:
        earlier_date = compare_dates(date_e, date_f)
        print(earlier_date)
    except ValueError as e:
        print(f"Error: {e}")
    date_g = "2023/10/26"
    date_h = "2023-10-25"
    try:
        earlier_date = compare_dates(date_g, date_h)
        print(earlier_date)
    except ValueError as e:
        print(f"Error: {e}")