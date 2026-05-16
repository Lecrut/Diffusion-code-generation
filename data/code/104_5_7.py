from datetime import datetime
def is_strictly_before(date_str1, date_str2):
    date1 = datetime.strptime(date_str1, '%Y-%m-%d')
    date2 = datetime.strptime(date_str2, '%Y-%m-%d')
    return date1 < date2
if __name__ == '__main__':
    date1_str = "2023-01-15"
    date2_str = "2023-01-20"
    result1 = is_strictly_before(date1_str, date2_str)
    print(f"{date1_str} is strictly before {date2_str}: {result1}")
    date1_str = "2023-12-31"
    date2_str = "2024-01-01"
    result2 = is_strictly_before(date1_str, date2_str)
    print(f"{date1_str} is strictly before {date2_str}: {result2}")
    date1_str = "2024-05-10"
    date2_str = "2024-5-10"
    result3 = is_strictly_before(date1_str, date2_str)
    print(f"{date1_str} is strictly before {date2_str}: {result3}")
    date1_str = "2024-05-10"
    date2_str = "2024-5-10"
    result4 = is_strictly_before(date2_str, date1_str)
    print(f"{date2_str} is strictly before {date1_str}: {result4}")