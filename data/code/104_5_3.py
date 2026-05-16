from datetime import datetime
def is_strictly_before(date_str1, date_str2):
    date1 = datetime.strptime(date_str1, "%Y-%m-%d")
    date2 = datetime.strptime(date_str2, "%Y-%m-%d")
    return date1 < date2
if __name__ == '__main__':
    date1_str = "2023-01-15"
    date2_str = "2023-02-01"
    result1 = is_strictly_before(date1_str, date2_str)
    print(result1)
    date1_str = "2023-02-01"
    date2_str = "2023-01-15"
    result2 = is_strictly_before(date1_str, date2_str)
    print(result2)
    date1_str = "2023-10-20"
    date2_str = "2023-10-20"
    result3 = is_strictly_before(date1_str, date2_str)
    print(result3)
    date1_str = "2024-01-01"
    date2_str = "2024-01-02"
    result4 = is_strictly_before(date1_str, date2_str)
    print(result4)