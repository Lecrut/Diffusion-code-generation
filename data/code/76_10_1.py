from datetime import datetime
def calculate_days(date_str1, date_str2):
    try:
        date1 = datetime.strptime(date_str1, '%Y-%m-%d')
        date2 = datetime.strptime(date_str2, '%Y-%m-%d')
        diff = abs(date1 - date2)
        return diff.days
    except TypeError:
        return -1
    except ValueError:
        return -2
if __name__ == '__main__':
    date1_str = "2023-01-01"
    date2_str = "2023-01-10"
    result = calculate_days(date1_str, date2_str)
    print(result)
    date3_str = "2024-12-31"
    date4_str = "2024-01-01"
    result2 = calculate_days(date3_str, date4_str)
    print(result2)
    date5_str = "2023-05-15"
    date6_str = "2023-05-15"
    result3 = calculate_days(date5_str, date6_str)
    print(result3)