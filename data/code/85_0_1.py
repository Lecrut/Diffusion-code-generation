import datetime
def calculate_week_difference(date_str1, date_str2):
    date1 = datetime.datetime.strptime(date_str1, '%Y-%m-%d')
    date2 = datetime.datetime.strptime(date_str2, '%Y-%m-%d')
    time_difference = abs(date1 - date2)
    weeks = time_difference.days / 7.0
    return weeks
if __name__ == '__main__':
    date1_str = "2023-01-01"
    date2_str = "2023-01-08"
    result = calculate_week_difference(date1_str, date2_str)
    print(result)