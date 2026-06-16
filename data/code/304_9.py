import datetime
def is_strictly_earlier(date_str1, date_str2):
    date1 = datetime.datetime.strptime(date_str1, "%Y-%m-%d").date()
    date2 = datetime.datetime.strptime(date_str2, "%Y-%m-%d").date()
    return date1 < date2
if __name__ == '__main__':
    date_a = "2023-01-15"
    date_b = "2023-01-16"
    print(is_strictly_earlier(date_a, date_b))
    date_c = "2024-05-20"
    date_d = "2024-05-20"
    print(is_strictly_earlier(date_c, date_d))
    date_e = "2023-12-31"
    date_f = "2023-12-30"
    print(is_strictly_earlier(date_e, date_f))