import datetime
def compare_dates(date_str1, date_str2):
    try:
        date1 = datetime.datetime.strptime(date_str1, '%Y-%m-%d')
        date2 = datetime.datetime.strptime(date_str2, '%Y-%m-%d')
        return "Date 1 is later than Date 2" if date1 > date2 else "Date 2 is later than Date 1" if date2 > date1 else "The dates are equal"
    except ValueError:
        return "Error: One or both date strings are in an invalid format. Please use YYYY-MM-DD."
if __name__ == '__main__':
    date_a = "2023-10-26"
    date_b = "2023-10-25"
    print(compare_dates(date_a, date_b))
    date_c = "2024-01-01"
    date_d = "2024-01-01"
    print(compare_dates(date_c, date_d))
    date_e = "2023/10/26"
    date_f = "2023-10-25"
    print(compare_dates(date_e, date_f))