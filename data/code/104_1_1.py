from datetime import datetime
def compare_dates(date_str1, date_str2):
    dt1 = datetime.strptime(date_str1, '%Y-%m-%d')
    dt2 = datetime.strptime(date_str2, '%Y-%m-%d')
    if dt1 > dt2:
        return dt1.strftime('%Y-%m-%d')
    else:
        return dt2.strftime('%Y-%m-%d')
if __name__ == '__main__':
    date1 = "2023-10-26"
    date2 = "2023-10-20"
    result = compare_dates(date1, date2)
    print(result)
    date3 = "2024-01-01"
    date4 = "2024-01-15"
    result2 = compare_dates(date3, date4)
    print(result2)
    date5 = "2022-12-31"
    date6 = "2022-12-31"
    result3 = compare_dates(date5, date6)
    print(result3)