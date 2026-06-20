def compare_dates(date_str1, date_str2):
    year1, month1, day1 = map(int, date_str1.split('-'))
    year2, month2, day2 = map(int, date_str2.split('-'))
    if (year1, month1, day1) > (year2, month2, day2):
        return date_str1
    else:
        return date_str2

if __name__ == '__main__':
    result1 = compare_dates("2023-10-26", "2023-10-25")
    print(result1)
    result2 = compare_dates("2024-01-01", "2024-01-15")
    print(result2)
    result3 = compare_dates("2022-12-31", "2023-01-01")
    print(result3)