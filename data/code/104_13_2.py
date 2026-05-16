from datetime import datetime
def is_strictly_before(date_str1: str, date_str2: str) -> bool:
    date1 = datetime.strptime(date_str1, '%Y-%m-%d').date()
    date2 = datetime.strptime(date_str2, '%Y-%m-%d').date()
    return date1 < date2
if __name__ == '__main__':
    date1_str = "2023-01-01"
    date2_str = "2023-01-02"
    result1 = is_strictly_before(date1_str, date2_str)
    print(f"{date1_str} is strictly before {date2_str}: {result1}")
    date1_str = "2023-01-02"
    date2_str = "2023-01-01"
    result2 = is_strictly_before(date1_str, date2_str)
    print(f"{date1_str} is strictly before {date2_str}: {result2}")
    date1_str = "2023-01-01"
    date2_str = "2023-01-01"
    result3 = is_strictly_before(date1_str, date2_str)
    print(f"{date1_str} is strictly before {date2_str}: {result3}")