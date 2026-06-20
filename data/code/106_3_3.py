import datetime

def calculate_age_difference(date_str1, date_str2):
    try:
        date_format = "%Y-%m-%d"
        date1 = datetime.datetime.strptime(date_str1, date_format)
        date2 = datetime.datetime.strptime(date_str2, date_format)
        age_diff = abs((date2 - date1).days) // 365
        return age_diff
    except ValueError:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")

if __name__ == '__main__':
    date1 = "1990-05-15"
    date2 = "2023-04-10"
    print(calculate_age_difference(date1, date2))