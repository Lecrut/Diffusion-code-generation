import datetime

def calculate_year_difference(date_str1, date_str2):
    date_format = "%Y-%m-%d"
    date1 = datetime.datetime.strptime(date_str1, date_format)
    date2 = datetime.datetime.strptime(date_str2, date_format)
    return abs((date2 - date1).days // 365)

if __name__ == '__main__':
    a = "2023-04-01"
    b = "1998-11-15"
    result = calculate_year_difference(a, b)
    print(result)