import datetime
def calculate_week_difference(date_str1, date_str2):
    date1 = datetime.datetime.strptime(date_str1, '%Y-%m-%d')
    date2 = datetime.datetime.strptime(date_str2, '%Y-%m-%d')
    time_difference = abs(date1 - date2)
    difference_in_days = time_difference.days
    weeks = difference_in_days / 7.0
    return weeks
if __name__ == '__main__':
    date1 = "2023-01-01"
    date2 = "2023-01-08"
    result = calculate_week_difference(date1, date2)
    print(result)