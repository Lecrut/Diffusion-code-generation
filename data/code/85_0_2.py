import datetime
def calculate_week_difference(date_str1, date_str2):
    date1 = datetime.datetime.strptime(date_str1, '%Y-%m-%d')
    date2 = datetime.datetime.strptime(date_str2, '%Y-%m-%d')
    time_difference = abs(date2 - date1)
    weeks = time_difference.days / 7.0
    return weeks
if __name__ == '__main__':
    date1 = "2023-01-01"
    date2 = "2023-01-08"
    difference = calculate_week_difference(date1, date2)
    print(difference)