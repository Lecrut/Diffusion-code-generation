import datetime
def compare_dates(date_str1, date_str2):
    try:
        date1 = datetime.datetime.strptime(date_str1, '%Y-%m-%d')
        date2 = datetime.datetime.strptime(date_str2, '%Y-%m-%d')
        if date1 < date2:
            return f"{date_str1} is earlier than {date_str2}"
        elif date2 < date1:
            return f"{date_str2} is earlier than {date_str1}"
        else:
            return f"{date_str1} and {date_str2} are the same date"
    except ValueError:
        return "Error: Invalid date format. Please use YYYY-MM-DD."
if __name__ == '__main__':
    date_a = "2023-10-25"
    date_b = "2023-10-15"
    result = compare_dates(date_a, date_b)
    print(result)
    date_c = "2024-01-01"
    date_d = "2023-12-31"
    result2 = compare_dates(date_c, date_d)
    print(result2)
    date_e = "2023/10/25"
    date_f = "2023-10-15"
    result3 = compare_dates(date_e, date_f)
    print(result3)