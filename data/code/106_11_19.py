from datetime import datetime

def calculate_year_difference(date_str1, date_str2):
    date_format = "%Y-%m-%d"
    date1 = datetime.strptime(date_str1, date_format)
    date2 = datetime.strptime(date_str2, date_format)
    return abs((date1 - date2).days) // 365

if __name__ == '__main__':
    date1 = "2023-10-05"
    date2 = "1998-07-14"
    difference = calculate_year_difference(date1, date2)
    print(difference)