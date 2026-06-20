def compare_dates(date_str1, date_str2):
    year1, month1, day1 = map(int, date_str1.split('-'))
    year2, month2, day2 = map(int, date_str2.split('-'))
    if (year1, month1, day1) > (year2, month2, day2):
        return 1
    elif (year1, month1, day1) < (year2, month2, day2):
        return -1
    else:
        return 0

if __name__ == '__main__':
    result = compare_dates("2023-10-26", "2023-10-25")
    print(result)