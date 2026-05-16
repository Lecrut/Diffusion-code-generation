import datetime
def calculate_days(date_str1, date_str2):
    date1 = datetime.datetime.strptime(date_str1, '%Y-%m-%d')
    date2 = datetime.datetime.strptime(date_str2, '%Y-%m-%d')
    return abs((date1 - date2).days)
if __name__ == '__main__':
    date1 = "2023-01-01"
    date2 = "2023-01-10"
    result = calculate_days(date1, date2)
    print(result)