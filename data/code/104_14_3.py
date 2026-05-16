import datetime
def compare_dates(date_str1, date_str2):
    try:
        date1 = datetime.datetime.strptime(date_str1, '%Y-%m-%d')
        date2 = datetime.datetime.strptime(date_str2, '%Y-%m-%d')
        if date1 > date2:
            return f"{date_str1} is after {date_str2}"
        elif date1 < date2:
            return f"{date_str1} is before {date_str2}"
        else:
            return f"{date_str1} is equal to {date_str2}"
    except ValueError:
        return "Error: One or both date strings are in an invalid format. Please use YYYY-MM-DD."
if __name__ == '__main__':
    date_a = "2023-10-26"
    date_b = "2023-10-25"
    print(compare_dates(date_a, date_b))
    date_c = "2024-01-01"
    date_d = "2024-01-01"
    print(compare_dates(date_c, date_d))
    date_e = "2022/12/31"
    date_f = "2023-01-01"
    print(compare_dates(date_e, date_f))
    date_g = "2023-10-26"
    date_h = "InvalidDate"
    print(compare_dates(date_g, date_h))