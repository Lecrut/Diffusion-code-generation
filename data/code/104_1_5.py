import datetime
def compare_dates(date_str1, date_str2):
    date1 = datetime.datetime.strptime(date_str1, "%Y-%m-%d")
    date2 = datetime.datetime.strptime(date_str2, "%Y-%m-%d")
    if date1 > date2:
        return date1.strftime("%Y-%m-%d")
    else:
        return date2.strftime("%Y-%m-%d")
if __name__ == '__main__':
    date_a = "2023-10-25"
    date_b = "2023-11-01"
    result1 = compare_dates(date_a, date_b)
    print(result1)
    date_c = "2024-01-15"
    date_d = "2024-01-10"
    result2 = compare_dates(date_c, date_d)
    print(result2)
    date_e = "2022-12-31"
    date_f = "2022-12-31"
    result3 = compare_dates(date_e, date_f)
    print(result3)