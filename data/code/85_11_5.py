import datetime
def calculate_week_difference(date_str1, date_str2):
    date1 = datetime.datetime.strptime(date_str1, '%Y-%m-%d').date()
    date2 = datetime.datetime.strptime(date_str2, '%Y-%m-%d').date()
    diff = abs(date2 - date1)
    weeks = diff.days // 7
    return weeks
if __name__ == '__main__':
    date1_str = "2023-01-01"
    date2_str = "2023-01-08"
    result1 = calculate_week_difference(date1_str, date2_str)
    print(result1)
    date3_str = "2023-01-01"
    date4_str = "2023-01-07"
    result2 = calculate_week_difference(date3_str, date4_str)
    print(result2)
    date5_str = "2023-01-01"
    date6_str = "2023-01-01"
    result3 = calculate_week_difference(date5_str, date6_str)
    print(result3)
    date7_str = "2023-01-01"
    date8_str = "2023-01-01"
    result4 = calculate_week_difference(date7_str, date8_str)
    print(result4)
    date9_str = "2023-01-01"
    date10_str = "2023-01-08"
    result5 = calculate_week_difference(date9_str, date10_str)
    print(result5)