import datetime
def calculate_date_difference(date_str1, date_str2):
    date1 = datetime.datetime.strptime(date_str1, '%Y-%m-%d')
    date2 = datetime.datetime.strptime(date_str2, '%Y-%m-%d')
    difference = abs(date1 - date2)
    return difference.days
if __name__ == '__main__':
    date1_str = "2023-01-01"
    date2_str = "2023-01-31"
    result = calculate_date_difference(date1_str, date2_str)
    print(result)