import datetime
def calculate_day_difference(date_str1, date_str2):
    date1 = datetime.datetime.strptime(date_str1, "%Y-%m-%d")
    date2 = datetime.datetime.strptime(date_str2, "%Y-%m-%d")
    difference = abs(date2 - date1)
    return difference.days
if __name__ == '__main__':
    date1_str = "2020-03-01"
    date2_str = "2024-03-01"
    result = calculate_day_difference(date1_str, date2_str)
    print(result)