import datetime
def calculate_week_difference(date_str1, date_str2):
    date1 = datetime.datetime.strptime(date_str1, '%Y-%m-%d').date()
    date2 = datetime.datetime.strptime(date_str2, '%Y-%m-%d').date()
    difference = abs(date2 - date1)
    weeks = (difference.days // 7)
    return weeks
if __name__ == '__main__':
    date1_str = "2023-01-01"
    date2_str = "2023-01-08"
    result1 = calculate_week_difference(date1_str, date2_str)
    print(result1)
    date1_str = "2023-01-01"
    date2_str = "2023-01-07"
    result2 = calculate_week_difference(date1_str, date2_str)
    print(result2)
    date1_str = "2023-01-01"
    date2_str = "2023-01-01"
    result3 = calculate_week_difference(date1_str, date2_str)
    print(result3)
    date1_str = "2023-01-01"
    date2_str = "2023-01-08"
    result4 = calculate_week_difference(date2_str, date1_str)
    print(result4)
    date1_str = "2023-12-31"
    date2_str = "2024-01-01"
    result5 = calculate_week_difference(date1_str, date2_str)
    print(result5)