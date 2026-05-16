import datetime
def calculate_days(date_str1, date_str2):
    date1 = datetime.datetime.strptime(date_str1, '%Y-%m-%d')
    date2 = datetime.datetime.strptime(date_str2, '%Y-%m-%d')
    return abs((date1 - date2).days)
if __name__ == '__main__':
    date1_str = "2023-01-01"
    date2_str = "2023-01-10"
    result = calculate_days(date1_str, date2_str)
    print(result)