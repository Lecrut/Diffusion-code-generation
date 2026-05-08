import datetime
def is_strictly_before(date_str1, date_str2):
    date1 = datetime.datetime.strptime(date_str1, '%Y-%m-%d').date()
    date2 = datetime.datetime.strptime(date_str2, '%Y-%m-%d').date()
    return date1 < date2
if __name__ == '__main__':
    date1_str = "2023-01-15"
    date2_str = "2023-01-16"
    result1 = is_strictly_before(date1_str, date2_str)
    print(f"{date1_str} is strictly before {date2_str}: {result1}")
    date1_str = "2023-01-16"
    date2_str = "2023-01-15"
    result2 = is_strictly_before(date1_str, date2_str)
    print(f"{date1_str} is strictly before {date2_str}: {result2}")
    date1_str = "2023-01-15"
    date2_str = "2023-01-15"
    result3 = is_strictly_before(date1_str, date2_str)
    print(f"{date1_str} is strictly before {date2_str}: {result3}")