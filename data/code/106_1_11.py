import datetime

def calculate_year_difference(date1_str, date2_str):
    date_format = "%Y-%m-%d"
    date1 = datetime.datetime.strptime(date1_str, date_format)
    date2 = datetime.datetime.strptime(date2_str, date_format)
    difference = abs((date2 - date1).days) // 365
    return difference

if __name__ == '__main__':
    print(calculate_year_difference("2023-04-15", "1990-07-23"))
    print(calculate_year_difference("2000-12-25", "2024-01-01"))
    print(calculate_year_difference("1850-11-07", "1900-06-05"))